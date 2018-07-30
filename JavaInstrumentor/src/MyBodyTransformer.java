import java.rmi.UnexpectedException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import org.jboss.util.NotImplementedException;
import org.omg.CORBA.UnionMember;

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
import soot.UnknownType;
import soot.Scene;
import soot.SootClass;
import soot.SootField;
import soot.SootMethod;
import soot.SootMethodRef;
import soot.Type;
import soot.Unit;
import soot.Value;
import soot.ValueBox;
import soot.grimp.NewInvokeExpr;
import soot.jimple.FieldRef;
import soot.jimple.IntConstant;
import soot.jimple.InvokeExpr;
import soot.jimple.Jimple;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;
import soot.jimple.internal.JInstanceFieldRef;
import soot.jimple.internal.JArrayRef;;

public class MyBodyTransformer extends BodyTransformer {
	public static String MY_PRIMITIVE_LOCAL_NAME = "mylocal", MY_REF_LOCAL_NAME = "$mylocal", OBJECT_TYPE = "java.lang.Object";
	private static Local myPrimitiveLocal, myRefLocal;
	
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
	
	private Map<String, Local> locals;
	
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
	
	private void patchAssignField(CaseAssign assignment, Unit anchor, PatchingChain<Unit> methodUnits, SootMethodRef updaterMethodRef) {
		FieldRef fielfRef = (FieldRef)assignment.lhs;
		Value mylocal = Selection.isPrimitive(fielfRef) ? myPrimitiveLocal : myRefLocal;
		Value rval = Selection.isPrimitive(fielfRef) ? fielfRef : StringConstant.v(fielfRef.toString());
		try {
		Stmt assignTmpStmt = Jimple.v().newAssignStmt(mylocal, fielfRef);
		
		Stmt invokeStmt = 
				Jimple.v().newInvokeStmt(
						Jimple.v().newStaticInvokeExpr(
								updaterMethodRef, 
								StringConstant.v(assignment.lhs.toString()),
								rval
								)
						);
		
		methodUnits.insertAfter(assignTmpStmt, anchor);
		anchor = assignTmpStmt;
		methodUnits.insertAfter(invokeStmt, anchor);
		} catch(Exception e) {
			System.out.println(fielfRef);
			int i = 0;
			System.out.println(i);
		}
	}
	
	private void patchAssignNormal(CaseAssign assignment, Unit anchor, PatchingChain<Unit> methodUnits, SootMethodRef updaterMethodRef) {
		Value r = Selection.isPrimitive(assignment.lhs) ? assignment.lhs : StringConstant.v(assignment.rhs.toString());
		
		Stmt invokeStmt = 
				Jimple.v().newInvokeStmt(
						Jimple.v().newStaticInvokeExpr(
								updaterMethodRef,
								StringConstant.v(assignment.lhs.toString()),
								r
								)
						);
		
		methodUnits.insertAfter(invokeStmt, anchor);
	}
	
	private void patchAssignArray(CaseAssign assignment, Unit anchor, PatchingChain<Unit> methodUnits, SootMethodRef updaterMethodRef) {
		System.err.println("we do not support arrays yet");
	}
	
	private void dispatchAssignment(CaseAssign assignment, Unit patchedUnit, PatchingChain<Unit> methodUnits, SootMethodRef updaterMethodRef) {
		Value lval = assignment.lhs;
		if (lval instanceof JInstanceFieldRef) patchAssignField(assignment, patchedUnit, methodUnits, updaterMethodRef);
		else if (lval instanceof JArrayRef) patchAssignArray(assignment, patchedUnit, methodUnits, updaterMethodRef);
		else patchAssignNormal(assignment, patchedUnit, methodUnits, updaterMethodRef);
	}

	private void patchAssignment(Unit patchedUnit, Map<String, Local> methodLocals, SootMethod method, CaseAssign assignment) {
		Value lval = assignment.lhs;
		Value rval = assignment.rhs;
		SootMethod updaterMethod = Selection.isPrimitive(lval) ? updateAssignmentPrimitive : updateAssignmentObject;
		dispatchAssignment(assignment, patchedUnit, method.getActiveBody().getUnits(), updaterMethod.makeRef());
	}

	private void applyPatch(Unit patchedUnit, SootMethod method, Map<String, Local> methodLocals) throws UnexpectedException {
		PatchingChain<Unit> methodUnits = method.getActiveBody().getUnits();
		Case<Unit> c = Selection.MatchUnit(patchedUnit);

		if (Selection.isAssignStmt(c)) patchAssignment(patchedUnit, methodLocals, method, (CaseAssign)c);
		else if (Selection.isInvokeStmt(c)) patchInvoke(patchedUnit, methodUnits, (CaseInvoke)c);
		else if (Selection.isReturnStmt(c)) patchReturn(patchedUnit, method);

//		else throw new UnexpectedException("unknown case " + c.getClass().getName());
	}

	public static Map<String, Local> mapLocals(Body body) {
		Map<String, Local> map = new HashMap<String, Local>();
		
		for (Local local : body.getLocals())
			if (!Selection.shouldIgnoreLocal(local))
				map.put(local.getName(), local);
		
		return map;
	}

	public void addInitExamplePatch(SootMethod method) {

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
	
	public void addInitLocalsPatch(SootMethod method, Unit anchor) {
		for (Local local : locals.values()) {
			if (!Selection.shouldIgnoreLocal(local)) {
				InvokeExpr exp = Jimple.v().newStaticInvokeExpr(
						initLocalMethod.makeRef(), 
						StringConstant.v(local.getName()), 
						IntConstant.v(Selection.isPrimitive(local) ? 1 : 0)
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
	
	private void getMethodSignatureSpec(SootMethod method) {
		String[] second = method.getSignature().split(": ")[1].split(" ");
		StringBuilder ans = new StringBuilder(second[1].split("\\(")[0]);
		ans.append("(");

		Set<String> set = locals.keySet();
		int i = 0;
		for(String s : set) {
			ans.append("mut ");
			ans.append(s);
			ans.append(":");
			ans.append(locals.get(s).getType());
			if(i != set.size()-1) {
				ans.append(" , ");
			}
			i++;
		}
		ans.append(") -> (returnLocal:");
		ans.append(second[0]);
		ans.append(")");
		
		System.out.printf(ans+"\n"); // <tests.factorial: int fact(int)>
	}

	@Override
	protected void internalTransform(Body body, String phaseName, Map<String, String> options) {		
		SootMethod method = body.getMethod();
		if (Selection.shouldIgnoreMethod(method)) {
			System.err.printf("ignoring %s\n", method.getSignature());
			return;
		} else System.out.printf("patching %s\n", method.getSignature());
		

		mapTypes(method.getDeclaringClass());
		
		locals = mapLocals(body);
		addMyLocals(body);
		getMethodSignatureSpec(method);
		
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

	private void addMyLocals(Body body) {
		myPrimitiveLocal = Jimple.v().newLocal(MY_PRIMITIVE_LOCAL_NAME, IntType.v());
		myRefLocal = Jimple.v().newLocal(MY_REF_LOCAL_NAME, RefType.v(OBJECT_TYPE));
		body.getLocals().add(myPrimitiveLocal);
		body.getLocals().add(myRefLocal);
	}
}
