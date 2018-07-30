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
import soot.SootField;
import soot.SootMethod;
import soot.Type;
import soot.Unit;
import soot.ValueBox;
import soot.grimp.NewInvokeExpr;
import soot.jimple.IntConstant;
import soot.jimple.InvokeExpr;
import soot.jimple.Jimple;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;

public class MyBodyTransformer extends BodyTransformer {
	static SootClass traceClass;
	static SootMethod 
	updateAssignmentPrimitive, 
	updateAssignmentObject, 
	updateInvoke, 
	updateReturn, 
	initExample,
	initLocalMethod,
	finishedInitLocalsMethod,
	finishMethod;

	static {
		traceClass = Scene.v().loadClassAndSupport(Trace.CLASS_NAME);
		//		for (SootMethod m : traceClass.getMethods()) System.out.println(m.getName());
		updateAssignmentPrimitive = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_PRIMITIVE_METHOD);
		updateAssignmentObject = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_OBJECT_METHOD);
		updateInvoke = traceClass.getMethodByName(Trace.UPDATE_INVOKE_METHOD);
		updateReturn = traceClass.getMethodByName(Trace.UPDATE_RETURN_METHOD);
		initExample = traceClass.getMethodByName(Trace.INIT_EXAMPLE_METHOD);
		initLocalMethod = traceClass.getMethodByName(Trace.INIT_LOCAL_METHOD);
		finishedInitLocalsMethod = traceClass.getMethodByName(Trace.FINISHED_INIT_LOCALS_METHOD);
		finishMethod = traceClass.getMethodByName(Trace.FINISH_METHOD);
	}
	
	private static Stmt generateVoidInvocationStmt(SootMethod method) {
		InvokeExpr exp = Jimple.v().newStaticInvokeExpr(method.makeRef());
		Stmt stmt = Jimple.v().newInvokeStmt(exp);
		return stmt;
	}

	private void patchReturn(Unit patchedUnit, SootMethod method) {
		PatchingChain<Unit> units = method.getActiveBody().getUnits();

		units.insertBefore(generateVoidInvocationStmt(updateReturn), patchedUnit); // is it different when you return a value (return a + b)?

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
		
		System.out.println("-----------");
		System.out.println(varName);
		System.out.println(updaterMethod.makeRef());
		System.out.println(StringConstant.v(varName));
		System.out.println(methodLocals.get(varName));
		
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

//		else throw new UnexpectedException("unknown case " + c.getClass().getName());
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
			addInitLocalsPatch(method, unit);
			return;
		}
	}
	
	public static void addInitLocalsPatch(SootMethod method, Unit anchor) {
		for (Local local : method.getActiveBody().getLocals()) {
			if (!Selection.isTempVar(local.getName())) {
				InvokeExpr exp = Jimple.v().newStaticInvokeExpr(
						initLocalMethod.makeRef(), 
						StringConstant.v(local.getName()), 
						IntConstant.v(Selection.isTypePrimitive(local.getType()) ? 1 : 0)
						);
				Stmt stmt = Jimple.v().newInvokeStmt(exp);
				method.getActiveBody().getUnits().insertBefore(stmt, anchor);
			}
		}
		
		method.getActiveBody().getUnits().insertBefore(generateVoidInvocationStmt(finishedInitLocalsMethod), anchor);
	}

	private Stmt createFinishInvocation() {
		return generateVoidInvocationStmt(finishMethod);
	}
	
	private static void mapValue(SootField local) {
		if (local.getType() instanceof RefType) {
			System.out.printf("type %s {\n", local.getName());
			for (SootField field : RefType.v(local.getType().toString()).getSootClass().getFields()) {
//				System.out.println("field:");
//				System.out.println(f.getName());
//				System.out.println(f.getModifiers());
//				System.out.println(f.getSignature());
//				System.out.println(f.getSubSignature());
//				System.out.println(f.getDeclaringClass());
//				System.out.println(f.getType());
				mapValue(field);
			}
			System.out.println("}");
		}
		else System.out.printf("%s:%s\n",local.getName(), local.getType());
	}
	
	private static void mapTypes(SootClass sootClass) {
		System.out.printf("type %s {\n", sootClass);
		for (SootField field : sootClass.getFields()) {
			mapValue(field);
		}
		System.out.println("}");
	}
	
	private static void getMethodSignatureSpec(SootMethod method) {
		System.out.printf("signature: %s\n", method.getSignature().split(" ")); // <tests.factorial: int fact(int)>
	}

	@Override
	protected void internalTransform(Body body, String phaseName, Map<String, String> options) {		
		SootMethod method = body.getMethod();
		if (Selection.shouldIgnoreMethod(method)) {
			System.err.printf("ignoring %s\n", method.getSignature());
			return;
		} else System.out.printf("patching %s\n", method.getSignature());
		
		getMethodSignatureSpec(method);
		mapTypes(method.getDeclaringClass());
		
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
