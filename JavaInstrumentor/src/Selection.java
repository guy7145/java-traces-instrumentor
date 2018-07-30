import javax.lang.model.type.ArrayType;

import bgu.cs.util.Matcher;
import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseInvoke;
import bgu.cs.util.soot.CaseReturnStmt;
import bgu.cs.util.soot.CaseReturnVoidStmt;
import flyClasses.Example;
import flyClasses.Trace;
import soot.BooleanType;
import soot.ByteType;
import soot.CharType;
import soot.IntType;
import soot.LongType;
import soot.RefType;
import soot.SootClass;
import soot.SootMethod;
import soot.Type;
import soot.Unit;

public class Selection {
	static final String MAIN_SUB_SIGNATURE = "void main(java.lang.String[])";
	
	static Matcher<Unit> commandMatcher;
	static {
		commandMatcher = new Matcher<>();
		commandMatcher.addAllCasesFromPkg(bgu.cs.util.soot.JimpleCase.class.getPackage());
	}
	
	public static boolean isFlyClass(SootClass sootClass) {
		/* our classes that are loaded on the fly */
		String className = sootClass.getName();
		return className.equals(Trace.CLASS_NAME) || className.equals(Example.CLASS_NAME);
	}
	
	public static boolean isSpecialMethod(SootMethod method) {
		/* methods like <init> and <clinit> */
		String methodName = method.getName();
		return methodName.charAt(0) == '<' && methodName.charAt(methodName.length() - 1) == '>';
	}
	
	public static boolean isMainMethod(SootMethod method) {
		return method.getSubSignature().equals(MAIN_SUB_SIGNATURE);
	}
	
	public static boolean shouldIgnoreMethod(SootMethod method) {
		return isFlyClass(method.getDeclaringClass()) || isSpecialMethod(method);
	}
	
	public static boolean isReturnStmt(Case<Unit> c) {
		return c instanceof CaseReturnStmt || c instanceof CaseReturnVoidStmt;
	}
	
	public static boolean isAssignStmt(Case<Unit> c) {
		return c instanceof CaseAssign;
	}
	
	public static boolean isInvokeStmt(Case<Unit> c) {
		return c instanceof CaseInvoke;
	}
	
	public static boolean isTempVar(String varName) {
		// $r1
		return varName.length() >= 3 && varName.charAt(0) == '$' && varName.charAt(1) != '$';
	}
	
	public static boolean shouldIgnoreUnit(Unit unit) {
		Case<Unit> c = commandMatcher.match(unit);
		if (isAssignStmt(c)) {
			String varName = ((CaseAssign)c).lhs.toString();
			if (!isTempVar(varName)) return false; // the variable was actually defined in the instrumented program
		} else if (isInvokeStmt(c) || isReturnStmt(c)) return false;
		
		return true;
	}
	
	public static boolean isTypePrimitive(Type type) {
		return !(type instanceof RefType || type instanceof ArrayType);
	}
	
	public static Case<Unit> MatchUnit(Unit unit) {
		return commandMatcher.match(unit);
	}
}
