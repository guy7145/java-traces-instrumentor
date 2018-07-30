import bgu.cs.util.Matcher;
import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseInvoke;
import bgu.cs.util.soot.CaseReturnStmt;
import bgu.cs.util.soot.CaseReturnVoidStmt;
import flyClasses.Example;
import flyClasses.Trace;
import soot.ArrayType;
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
import soot.Value;
import soot.jimple.internal.JInstanceFieldRef;

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
//		return varName.length() >= 3 && varName.charAt(0) == '$' && varName.charAt(1) != '$';
		return varName.equals(MyBodyTransformer.MY_PRIMITIVE_LOCAL_NAME)
				|| varName.equals(MyBodyTransformer.MY_REF_LOCAL_NAME);
	}
	
	public static boolean shouldIgnoreUnit(Unit unit) {
		Case<Unit> c = commandMatcher.match(unit);
		if (isAssignStmt(c)) {
			String varName = ((CaseAssign)c).lhs.toString();
			if (!isTempVar(varName)) return false; // the variable was actually defined in the instrumented program
		} else if (isInvokeStmt(c) || isReturnStmt(c)) return false;
		
		return true;
	}
	
	public static boolean isPrimitive(Value val) {
		Type valType = val.getType();
		boolean isPrimitive = !(valType instanceof RefType || valType instanceof ArrayType);

		System.out.println(valType);
		System.out.println(valType instanceof RefType);
		System.out.println(valType instanceof ArrayType);
		System.out.printf("type of %s is %s (%s)\n", val.toString(), val.getType(), isPrimitive ? "Primitive" : "RefType");

		return isPrimitive;
	}
	
	public static Case<Unit> MatchUnit(Unit unit) {
		return commandMatcher.match(unit);
	}
}
