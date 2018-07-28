import java.io.PrintStream;
import java.rmi.UnexpectedException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import bgu.cs.util.Matcher;
import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseInvoke;
import bgu.cs.util.soot.CaseReturnStmt;
import bgu.cs.util.soot.CaseReturnVoidStmt;
import flyClasses.Trace;
import polyglot.ast.SourceFile;
import redundant.MyCounter;
import soot.Body;
import soot.BodyTransformer;
import soot.Local;
import soot.PatchingChain;
import soot.Scene;
import soot.SootClass;
import soot.SootMethod;
import soot.Type;
import soot.Unit;
import soot.Value;
import soot.coffi.method_info;
import soot.jimple.IntConstant;
import soot.jimple.InvokeExpr;
import soot.jimple.Jimple;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;
import soot.jimple.internal.JMulExpr;
import soot.jimple.internal.JimpleLocal;

public class MyBodyTransformer extends BodyTransformer {
	
	static SootClass traceClass;
	static SootMethod updateAssignmentPrimitive, updateAssignmentObject, updateInvoke, updateReturn;
	static Matcher<Unit> commandMatcher;
	
	static {
		traceClass = Scene.v().loadClassAndSupport(Trace.CLASS_NAME);
//		for (SootMethod m : traceClass.getMethods()) System.out.println(m.getName());
		updateAssignmentPrimitive = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_PRIMITIVE_METHOD);
		updateAssignmentObject = traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_OBJECT_METHOD);
		updateInvoke = traceClass.getMethodByName(Trace.UPDATE_INVOKE_METHOD);
		updateReturn = traceClass.getMethodByName(Trace.UPDATE_RETURN_METHOD);
		
		commandMatcher = new Matcher<>();
		commandMatcher.addAllCasesFromPkg(bgu.cs.util.soot.JimpleCase.class.getPackage());
	}
	
	private boolean isFlyClass(SootClass sootClass) {
		/* our classes that are loaded on the fly */
		String className = sootClass.getName();
		return className.equals(Trace.CLASS_NAME);
	}
	
	private boolean isSpecialMethod(SootMethod method) {
		/* methods like <init> and <clinit> */
		String methodName = method.getName();
		return methodName.charAt(0) == '<' && methodName.charAt(methodName.length() - 1) == '>';
	}
	
	private boolean shouldIgnoreMethod(SootMethod method) {
		return isFlyClass(method.getDeclaringClass()) || isSpecialMethod(method);
	}
	
	private boolean isReturnStmt(Case<Unit> c) {
		return c instanceof CaseReturnStmt || c instanceof CaseReturnVoidStmt;
	}
	
	private boolean isAssignStmt(Case<Unit> c) {
		return c instanceof CaseAssign;
	}
	
	private boolean isInvokeStmt(Case<Unit> c) {
		return c instanceof CaseInvoke;
	}
	
	private boolean shouldIgnoreUnit(Unit unit) {
		Case<Unit> c = commandMatcher.match(unit);
		if (isAssignStmt(c)) {
			String varName = ((CaseAssign)c).lhs.toString();
			if (varName.charAt(0) != '$') return false; // the variable was actually defined in the instrumented program
		} else if (isInvokeStmt(c) || isReturnStmt(c)) return false;
		
		return true;
	}
	
	private boolean isTypePrimitive(Type type) {
		return type.toString().equals("int");
	}
	
	private void applyPatch(Unit patchedUnit, SootMethod method, Map<String, Local> methodLocals) throws UnexpectedException {
		PatchingChain<Unit> methodUnits = method.getActiveBody().getUnits();
		InvokeExpr exp = null;
		Case<Unit> c = commandMatcher.match(patchedUnit);
		
		if (isAssignStmt(c)) {	
			CaseAssign assignment = (CaseAssign)c;
			String varName = assignment.lhs.toString();
			
			SootMethod updaterMethod = isTypePrimitive(assignment.lhs.getType()) ? updateAssignmentPrimitive : updateAssignmentObject;
			
			exp = Jimple.v().newStaticInvokeExpr(
					updaterMethod.makeRef(), 
					StringConstant.v(varName),
					methodLocals.get(varName)
					);
			Stmt stmt = Jimple.v().newInvokeStmt(exp);
			methodUnits.insertAfter(stmt, patchedUnit);
		}
		
		else if (isInvokeStmt(c)) {
			exp = Jimple.v().newStaticInvokeExpr(updateInvoke.makeRef());
			Stmt stmt = Jimple.v().newInvokeStmt(exp);
			methodUnits.insertAfter(stmt, patchedUnit);
		}
		
		else if (isReturnStmt(c)) {
			exp = Jimple.v().newStaticInvokeExpr(updateReturn.makeRef()); // is it different when you return a value (return a + b)?
		    Stmt stmt = Jimple.v().newInvokeStmt(exp);
			methodUnits.insertBefore(stmt, patchedUnit);
		}
		else throw new UnexpectedException("unknown case " + c.getClass().getName());
	}
	
	public static Map<String, Local> mapLocals(Body body) {
		Map<String, Local> map = new HashMap<String, Local>();
		
		for (Local local : body.getLocals()) {
			System.out.printf("name=%s\n", local.getName());
			map.put(local.getName(), local);
		}
		return map;
	}
	
	@Override
	protected void internalTransform(Body body, String phaseName, Map<String, String> options) {
		SootMethod method = body.getMethod();
		
		if (shouldIgnoreMethod(method)) {
			System.err.printf("ignoring %s\n", method.getSignature());
			return;
		} else System.out.printf("patching %s\n", method.getSignature());
		
		Map<String, Local> locals = mapLocals(body);
		
		int lineNumber = 1;
		Iterator<Unit> snapIter = method
				.getActiveBody()
				.getUnits()
				.snapshotIterator(); // snapshot is needed because we iterate the chain while changing it
		
		while (snapIter.hasNext()) {
			Unit unit = snapIter.next();
			boolean ignoreUnit = shouldIgnoreUnit(unit);
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
