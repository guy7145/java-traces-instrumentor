import java.rmi.UnexpectedException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseAssignFieldRef;
import bgu.cs.util.soot.CaseAssignInstanceFieldRef;
import bgu.cs.util.soot.CaseIdentityStmt;
import bgu.cs.util.soot.CaseIdentityStmtParameter;
import bgu.cs.util.soot.CaseIdentityStmtThis;
import bgu.cs.util.soot.CaseInvoke;
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
import soot.SootMethodRef;
import soot.Unit;
import soot.Value;
import soot.jimple.FieldRef;
import soot.jimple.InstanceFieldRef;
import soot.jimple.IntConstant;
import soot.jimple.InvokeExpr;
import soot.jimple.Jimple;
import soot.jimple.StaticFieldRef;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;
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
	finishMethod,
	defTypesMethod,
	setDeltaModeMethod;

	static {
		traceClass = Scene.v().loadClassAndSupport(Trace.CLASS_NAME);
		updateAssignmentPrimitive = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_PRIMITIVE_METHOD);
		updateAssignmentObject = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_OBJECT_METHOD);
		updateInvoke = traceClass.getMethodByName(Trace.UPDATE_INVOKE_METHOD);
		updateReturn = traceClass.getMethodByName(Trace.UPDATE_RETURN_METHOD);
		initExample = traceClass.getMethodByName(Trace.INIT_EXAMPLE_METHOD);
		initLocalMethod = traceClass.getMethodByName(Trace.INIT_LOCAL_METHOD);
		finishedInitLocalsMethod = traceClass.getMethodByName(Trace.FINISHED_INIT_LOCALS_METHOD);
		finishMethod = traceClass.getMethodByName(Trace.FINISH_METHOD);
		defTypesMethod = traceClass.getMethodByName(Trace.DEF_TYPES_METHOD);
		setDeltaModeMethod = traceClass.getMethodByName(Trace.SET_DELTA_MODE_METHOD);
	}

	private Map<String, Value> locals;
	private String[] userClasses;
	private boolean deltaOnly, reportInvokes;
	
	public MyBodyTransformer(String[] userClasses, boolean deltaOnly, boolean reportInvokes) {
		this.userClasses = userClasses;
		this.deltaOnly = deltaOnly;
		this.reportInvokes = reportInvokes;
	}

	private static Stmt generateVoidInvocationStmt(SootMethod method) {
		InvokeExpr exp = Jimple.v().newStaticInvokeExpr(method.makeRef());
		Stmt stmt = Jimple.v().newInvokeStmt(exp);
		return stmt;
	}

	private void patchReturn(Unit patchedUnit, SootMethod method) {
		PatchingChain<Unit> units = method.getActiveBody().getUnits();

		units.insertBefore(generateVoidInvocationStmt(updateReturn), patchedUnit); // is it different when you return a value (return a + b)?

		if (Selection.isMainMethod(method)) units.insertBefore(createFinishInvocation(), patchedUnit);
	}

	protected void patchInvoke(Unit patchedUnit, PatchingChain<Unit> methodUnits, CaseInvoke invocation) {
		// ignore
	}

	public static String getFieldName(FieldRef field) {
		String fieldName = field.getField().getName();
		String base;
		
		if (field instanceof StaticFieldRef) base = ((StaticFieldRef)field).getField().getDeclaringClass().getName();
		
		else if (field instanceof InstanceFieldRef) {
			base = ((InstanceFieldRef)field).getBase().toString();
		}
		else return field.toString();
			
		return base + "." + fieldName;
	}

	private void patchAssignField(CaseAssign assignment, Unit anchor, PatchingChain<Unit> methodUnits, SootMethodRef updaterMethodRef) {
		InstanceFieldRef fielfRef = (InstanceFieldRef)assignment.lhs;

		Value mylocal = Selection.isPrimitive(fielfRef) ? myPrimitiveLocal : myRefLocal;

		Stmt assignTmpStmt = Jimple.v().newAssignStmt(mylocal, fielfRef);

		Stmt invokeStmt = 
				Jimple.v().newInvokeStmt(
						Jimple.v().newStaticInvokeExpr(
								updaterMethodRef, 
								StringConstant.v(getFieldName(fielfRef)),
								mylocal
								)
						);

		methodUnits.insertAfter(assignTmpStmt, anchor);
		anchor = assignTmpStmt;
		methodUnits.insertAfter(invokeStmt, anchor);
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
		if (lval instanceof InstanceFieldRef) patchAssignField(assignment, patchedUnit, methodUnits, updaterMethodRef);
		else if (lval instanceof JArrayRef) patchAssignArray(assignment, patchedUnit, methodUnits, updaterMethodRef);
		else patchAssignNormal(assignment, patchedUnit, methodUnits, updaterMethodRef);
	}

	protected void patchAssignment(Unit patchedUnit, SootMethod method, CaseAssign assignment) {
		SootMethod updaterMethod = Selection.isPrimitive(assignment.lhs) ? updateAssignmentPrimitive : updateAssignmentObject;
		dispatchAssignment(assignment, patchedUnit, method.getActiveBody().getUnits(), updaterMethod.makeRef());
	}

	private void applyPatch(Unit patchedUnit, SootMethod method) throws UnexpectedException {
		PatchingChain<Unit> methodUnits = method.getActiveBody().getUnits();
		Case<Unit> c = Selection.MatchUnit(patchedUnit);

		if (Selection.isAssignStmt(c)) 
			patchAssignment(patchedUnit, method, (CaseAssign)c);
		
		else if (Selection.isInvokeStmt(c)) {
			if (reportInvokes)
				patchInvoke(patchedUnit, methodUnits, (CaseInvoke)c);
		}
		else if (Selection.isReturnStmt(c)) 
			patchReturn(patchedUnit, method);

		else throw new UnexpectedException("unknown case " + c.getClass().getName());
	}
	
	public Map<String, Value> mapLocals(Body body) {
		Map<String, Value> map = new HashMap<>();
		for (Local local : body.getLocals()) {
//			if (Selection.isObject(local.getType())) {
//				System.out.printf("%s:%s\n", local.getName(), local.getType());
//				mapClass(Selection.asObject(local.getType()));
//			}
			if (!Selection.shouldIgnoreLocal(local))
				map.put(local.getName(), local);
		}
		return map;
	}

	public void addInitExamplePatch(SootMethod method) {
		Stmt initExampleStmt = Jimple.v().newInvokeStmt(
				Jimple.v().newStaticInvokeExpr(
						initExample.makeRef(), 
						StringConstant.v(getMethodSignatureSpec(method))
						)
				);
		
		Stmt setTypesStmt = Jimple.v().newInvokeStmt(
				Jimple.v().newStaticInvokeExpr(
						defTypesMethod.makeRef(), 
						StringConstant.v(mapTypes())
						)
				);
		
		Stmt setDeltaStmt = Jimple.v().newInvokeStmt(
				Jimple.v().newStaticInvokeExpr(
						setDeltaModeMethod.makeRef(), 
						IntConstant.v(deltaOnly ? 1 : 0)
						)
				);
		
		PatchingChain<Unit> units = method.getActiveBody().getUnits();
		for (Unit unit : units) {
			if (Selection.MatchUnit(unit) instanceof CaseIdentityStmt) continue;
			units.insertBefore(setDeltaStmt, unit);
			units.insertBefore(setTypesStmt, unit);
			units.insertBefore(initExampleStmt, unit);
			addInitLocalsPatch(method, unit);
			return;
		}
	}
	
	public static String getVariableName(Value v) {
		if (v instanceof FieldRef) return getFieldName((FieldRef)v);
		else return v.toString();
	}

	public void addInitLocalsPatch(SootMethod method, Unit anchor) {
		for (Value local : locals.values()) {
			InvokeExpr exp = Jimple.v().newStaticInvokeExpr(
					initLocalMethod.makeRef(), 
					StringConstant.v(getVariableName(local)), 
					IntConstant.v(Selection.isPrimitive(local) ? 1 : 0)
					);
			Stmt stmt = Jimple.v().newInvokeStmt(exp);
			method.getActiveBody().getUnits().insertBefore(stmt, anchor);
		}

		method.getActiveBody().getUnits().insertBefore(generateVoidInvocationStmt(finishedInitLocalsMethod), anchor);
	}

	private Stmt createFinishInvocation() {
		return generateVoidInvocationStmt(finishMethod);
	}
	
	private String mapTypes() {
		StringBuilder sb = new StringBuilder();
		for (String className : userClasses) {
			SootClass sc = Scene.v().getSootClass(className);
			sb.append(String.format("%s {\n", sc.getName()));
			for (SootField f : sc.getFields()) sb.append(String.format("\t%s:%s\n", f.getName(), f.getType()));
			sb.append("}\n");
		}
		return sb.toString();
	}

	private String getMethodSignatureSpec(SootMethod method) {
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
		if(second[0].equals("void")) {
			ans.append(") -> ()");
		}else {
			ans.append(") -> (returnLocal:");
			ans.append(second[0]);
			ans.append(")");
		}

		return ans.toString();
	}

	@Override
	protected void internalTransform(Body body, String phaseName, Map<String, String> options) {		
		SootMethod method = body.getMethod();
		if (Selection.shouldIgnoreMethod(method)) return;
		System.out.printf("patching %s\n", method.getSignature());
		
		locals = mapLocals(body);
		addMyLocals(body);
		getMethodSignatureSpec(method);
		
		for (Unit unit : body.getUnits()) {
			Case<Unit> c = Selection.MatchUnit(unit);
			if (Selection.isAssignStmt(c)) {
				Value var = ((CaseAssign)c).lhs;
				if (!Selection.shouldIgnoreLocal(var)) {
					locals.put(getVariableName(var), var);
				}
			}
		}
		
		Iterator<Unit> snapIter = 
				body
				.getUnits()
				.snapshotIterator(); // snapshot is needed because we iterate the chain while changing it

		addInitExamplePatch(method);
		
		while (snapIter.hasNext()) {
			Unit unit = snapIter.next();
			boolean ignoreUnit = Selection.shouldIgnoreUnit(unit);

			if (!ignoreUnit) {
				try {
					applyPatch(unit, method);
				} catch (UnexpectedException e) {
					e.printStackTrace();
					System.exit(1999);
				}
			}
		}
	}

	private void addMyLocals(Body body) {
		myPrimitiveLocal = Jimple.v().newLocal(MY_PRIMITIVE_LOCAL_NAME, IntType.v());
		myRefLocal = Jimple.v().newLocal(MY_REF_LOCAL_NAME, RefType.v(OBJECT_TYPE));
		body.getLocals().add(myPrimitiveLocal);
		body.getLocals().add(myRefLocal);
	}
}
