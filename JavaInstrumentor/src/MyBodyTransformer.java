import java.rmi.UnexpectedException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import bgu.cs.util.Matcher;
import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseIdentityStmtParameter;
import bgu.cs.util.soot.CaseInvoke;
import bgu.cs.util.soot.CaseReturnStmt;
import bgu.cs.util.soot.CaseReturnVoidStmt;
import flyClasses.Example;
import flyClasses.Trace;
import soot.Body;
import soot.BodyTransformer;
import soot.IntType;
import soot.Local;
import soot.PatchingChain;
import soot.RefType;
import soot.Scene;
import soot.SootClass;
import soot.SootMethod;
import soot.Type;
import soot.Unit;
import soot.ValueBox;
import soot.jimple.IntConstant;
import soot.jimple.InvokeExpr;
import soot.jimple.Jimple;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;

public class MyBodyTransformer extends BodyTransformer {
	static SootClass traceClass;
	static SootMethod updateAssignmentPrimitive, updateAssignmentObject, updateInvoke, updateReturn, initExample, finishMethod;

	static {
		traceClass = Scene.v().loadClassAndSupport(Trace.CLASS_NAME);
		//		for (SootMethod m : traceClass.getMethods()) System.out.println(m.getName());
		updateAssignmentPrimitive = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_PRIMITIVE_METHOD);
		updateAssignmentObject = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_OBJECT_METHOD);
		updateInvoke = traceClass.getMethodByName(Trace.UPDATE_INVOKE_METHOD);
		updateReturn = traceClass.getMethodByName(Trace.UPDATE_RETURN_METHOD);
		initExample = traceClass.getMethodByName(Trace.INIT_EXAMPLE_METHOD);
		finishMethod = traceClass.getMethodByName(Trace.FINISH_METHOD);
	}

	private void patchReturn(Unit patchedUnit, SootMethod method) {
		PatchingChain<Unit> units = method.getActiveBody().getUnits();

		InvokeExpr exp = Jimple.v().newStaticInvokeExpr(updateReturn.makeRef()); // is it different when you return a value (return a + b)?
		Stmt stmt = Jimple.v().newInvokeStmt(exp);
		units.insertBefore(stmt, patchedUnit);

		if (Selection.isMainMethod(method)) {
			System.out.println("found main!");
			units.insertBefore(createFinishInvocation(), patchedUnit);
		}
	}

	private void patchInvoke(Unit patchedUnit, PatchingChain<Unit> methodUnits, CaseInvoke invocation) {
		InvokeExpr exp = Jimple.v().newStaticInvokeExpr(updateInvoke.makeRef(), StringConstant.v(invocation.invoke.toString()));
		Stmt stmt = Jimple.v().newInvokeStmt(exp);
		methodUnits.insertAfter(stmt, patchedUnit);
	}

	private void patchAssignment(Unit patchedUnit, Map<String, Local> methodLocals, PatchingChain<Unit> methodUnits, CaseAssign assignment) {
		String varName = assignment.lhs.toString();

		SootMethod updaterMethod = Selection.isTypePrimitive(assignment.lhs.getType()) ? updateAssignmentPrimitive : updateAssignmentObject;

		InvokeExpr exp = Jimple.v().newStaticInvokeExpr(
				updaterMethod.makeRef(), 
				StringConstant.v(varName),
				methodLocals.get(varName)
				);
		Stmt stmt = Jimple.v().newInvokeStmt(exp);
		methodUnits.insertAfter(stmt, patchedUnit);
	}

	private void applyPatch(Unit patchedUnit, SootMethod method, Map<String, Local> methodLocals) throws UnexpectedException {
		PatchingChain<Unit> methodUnits = method.getActiveBody().getUnits();
		Case<Unit> c = Selection.MatchUnit(patchedUnit);

		if (Selection.isAssignStmt(c)) patchAssignment(patchedUnit, methodLocals, methodUnits, (CaseAssign)c);
		else if (Selection.isInvokeStmt(c)) patchInvoke(patchedUnit, methodUnits, (CaseInvoke)c);
		else if (Selection.isReturnStmt(c)) patchReturn(patchedUnit, method);

		else throw new UnexpectedException("unknown case " + c.getClass().getName());
	}

	public static Map<String, Local> mapLocals(Body body) {
		Map<String, Local> map = new HashMap<String, Local>();

		for (Local local : body.getLocals()) map.put(local.getName(), local);

		return map;
	}

	public static void addInitExamplePatch(SootMethod method) {

		InvokeExpr exp = Jimple.v().newStaticInvokeExpr(initExample.makeRef(), StringConstant.v(method.getName()));
		Stmt stmt = Jimple.v().newInvokeStmt(exp);

		PatchingChain<Unit> units = method.getActiveBody().getUnits();
		for (Unit unit : units) {
			if (Selection.MatchUnit(unit) instanceof CaseIdentityStmtParameter) continue;
			units.insertBefore(stmt, unit);
			return;
		}
	}

	public static void addInitLocalsPatch() {

	}

	private Stmt createFinishInvocation() {
		InvokeExpr exp = Jimple.v().newStaticInvokeExpr(finishMethod.makeRef());
		Stmt stmt = Jimple.v().newInvokeStmt(exp);
		return stmt;
	}

	private static void mapClasses() {

	}

	private static void getMethodSignatureSpec(SootMethod method) {
		System.out.printf("signature: %s", method.getSignature());
	}

	@Override
	protected void internalTransform(Body body, String phaseName, Map<String, String> options) {		
		SootMethod method = body.getMethod();
		getMethodSignatureSpec(method);

		if (Selection.shouldIgnoreMethod(method)) {
			System.err.printf("ignoring %s\n", method.getSignature());
			return;
		} else System.out.printf("patching %s\n", method.getSignature());

		Map<String, Local> locals = mapLocals(body);

		int lineNumber = 1;
		Iterator<Unit> snapIter = method
				.getActiveBody()
				.getUnits()
				.snapshotIterator(); // snapshot is needed because we iterate the chain while changing it

		addInitExamplePatch(method);

		while (snapIter.hasNext()) {
			Unit unit = snapIter.next();
			boolean ignoreUnit = Selection.shouldIgnoreUnit(unit);
			(ignoreUnit ? System.err : System.out).printf("(%s)\t%d. %s\n", ignoreUnit ? "ignoring" : "recording", lineNumber++, unit);

			if (!ignoreUnit) {
				try {
					applyPatch(unit, method, locals);
				} catch (UnexpectedException e) {
					e.printStackTrace();
					System.exit(1999);
				}
			}
		}
		System.out.println("finished patching.");
	}
}
