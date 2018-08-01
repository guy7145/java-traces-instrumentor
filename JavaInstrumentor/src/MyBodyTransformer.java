import java.rmi.UnexpectedException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseAssignFieldRef;
import bgu.cs.util.soot.CaseAssignInstanceFieldRef;
import bgu.cs.util.soot.CaseAssignLocal_BinopExpr;
import bgu.cs.util.soot.CaseAssignLocal_InvokeInstance;
import bgu.cs.util.soot.CaseAssignLocal_NewExpr;
import bgu.cs.util.soot.CaseIdentityStmt;
import bgu.cs.util.soot.CaseIdentityStmtParameter;
import bgu.cs.util.soot.CaseIdentityStmtThis;
import bgu.cs.util.soot.CaseInvoke;
import bgu.cs.util.soot.CaseReturnStmt;
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
import soot.Type;
import soot.Unit;
import soot.Value;
import soot.VoidType;
import soot.jimple.BinopExpr;
import soot.jimple.FieldRef;
import soot.jimple.InstanceFieldRef;
import soot.jimple.IntConstant;
import soot.jimple.InvokeExpr;
import soot.jimple.Jimple;
import soot.jimple.StaticFieldRef;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;
import soot.jimple.internal.JArrayRef;
import soot.util.Chain;;

public class MyBodyTransformer extends BodyTransformer {
	public static String MY_PRIMITIVE_LOCAL_NAME = "mylocal", MY_REF_LOCAL_NAME = "$mylocal", OBJECT_TYPE = "java.lang.Object", ToString_METHOD_SUBSIGNATURE = "toString";
	private static Local myPrimitiveLocal, myRefLocal;

	static SootClass traceClass;
	static SootMethod 
	updateAssignmentPrimitive, 
	updateAssignmentObject, 
	updateInvoke, 
	updateReturn, 
	initExample,
	initLocalObjectMethod,
	initLocalPrimitiveMethod,
	initLocalDefaultMethod,
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
		initLocalObjectMethod = traceClass.getMethodByName(Trace.INIT_LOCAL_OBJECT_METHOD);
		initLocalPrimitiveMethod = traceClass.getMethodByName(Trace.INIT_LOCAL_PRIMITIVE_METHOD);
		initLocalDefaultMethod = traceClass.getMethodByName(Trace.INIT_LOCAL_DEFAULT_METHOD);
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
	
	public static String getVariableName(Value v) {
		if (v instanceof FieldRef) return getFieldName((FieldRef)v);
		else return v.toString();
	}
	
	protected static Value getRValJMinor(CaseAssign assignment) {
		Value rval = null;
		String stringVal = null;
		
		if (assignment instanceof CaseAssignLocal_BinopExpr) {
			BinopExpr bin_op = (BinopExpr)assignment.rhs;
			stringVal = getVariableName(bin_op.getOp1()) + bin_op.getSymbol() + getVariableName(bin_op.getOp2());
		} 
//		else if (assignment instanceof CaseAssignLocal_NewExpr) {
//			Chain<SootClass> classes = Scene.v().getClasses();
//			for (SootClass sc : classes) {
//				if (sc.getType().equals(assignment.lhs.getType()))
//					rval = Jimple.v().newSpecialInvokeExpr((Local)assignment.lhs, sc.getMethodByName(ToString_METHOD_SUBSIGNATURE).makeRef()); // is it necessarily a Local?
//			}
//			
//			if (rval == null) System.err.println("Warning: didn't find class Object (getRValJMinor)");
////			rval = assignment.lhs;
//		}
		
		if (rval == null && stringVal == null) 
			stringVal = getVariableName(assignment.rhs);
		
		return stringVal == null ? rval : StringConstant.v(stringVal);
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
		Value r = Selection.isPrimitive(assignment.lhs) ? assignment.lhs : getRValJMinor(assignment);
		
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
	
	private static Value getReturnValue(Body body) {
		Set<Value> values = new HashSet<>();
		Case<Unit> c;
		CaseReturnStmt retStmt;
		for (Unit unit : body.getUnits()) {
			c = Selection.MatchUnit(unit);
			if (Selection.isReturnStmt(c)) {
				retStmt = (CaseReturnStmt)c;
				values.add(retStmt.op);
			}
		}
		
		if (values.size() > 1) {
			System.err.println("Warning: more than one return value found. choosing the first one... (getReturnValue)");
		} else if (values.size() < 1) {
			System.err.println("Warning: no return values found. you shouldn't call \"getReturnValue\" on void methods...");
		}
		
		return values.iterator().next();
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
	
	public static Set<Value> getParameters(Body body) {
		Set<Value> params = new HashSet<>();
		loop:
		for (Unit unit : body.getUnits()) {
			Case<Unit> c = Selection.MatchUnit(unit);
			if (c instanceof CaseIdentityStmtParameter) {
				params.add(((CaseIdentityStmtParameter)c).lhs);
			} else if (!(c instanceof CaseIdentityStmt)) break loop; // once identity statements are over than we won't see another one again
		}
		
		return params;
	}

	public void addInitLocalsPatch(SootMethod method, Unit anchor) {
		Set<Value> params = getParameters(method.getActiveBody()); 
		
		for (Value local : locals.values()) {
			SootMethod initMethod;
			Value rvalue;
			
			boolean isParam = params.contains(local);
			boolean isPrimitive = Selection.isPrimitive(local);
			
			if (!isParam) initMethod = initLocalDefaultMethod;
			else if (isPrimitive) initMethod = initLocalPrimitiveMethod;
			else initMethod = initLocalObjectMethod;
			
			if (isParam) rvalue = local;
			else rvalue = IntConstant.v(isPrimitive ? 1 : 0);
			
			InvokeExpr exp = Jimple.v().newStaticInvokeExpr(
					initMethod.makeRef(),
					StringConstant.v(getVariableName(local)), 
					rvalue
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
			
			if (sc.getFields().size() == 0) continue;
			
			sb.append(String.format("%s {\n", sc.getName()));
			for (SootField f : sc.getFields()) sb.append(String.format("\t%s:%s\n", f.getName(), f.getType()));
			sb.append("}\n");
		}
		return sb.toString();
	}

	private String getMethodSignatureSpec(SootMethod method) {
		String returnSig = "";
		Type returnType = method.getReturnType();
		if(!(returnType instanceof VoidType)) {
			Value returnValue = getReturnValue(method.getActiveBody());
			returnSig = String.format("%s:%s", returnValue.toString(), returnType);
		}
		
		Set<Value> params = getParameters(method.getActiveBody());
		List<String> paramsSigs = new LinkedList<>();
		for(Value p : params) 
			paramsSigs.add(String.format("mut %s:%s", getVariableName(p), p.getType()));		
		
		String paramsSig = String.join(", ", paramsSigs);
		
		
		return String.format("%s(%s) -> (%s)", method.getName(), paramsSig, returnSig);
	}

	@Override
	protected void internalTransform(Body body, String phaseName, Map<String, String> options) {		
		SootMethod method = body.getMethod();
		if (Selection.shouldIgnoreMethod(method)) return;
		System.out.printf("patching %s\n", method.getSignature());
		
		locals = mapLocals(body);
		addMyLocals(body);
		
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
