import bgu.cs.util.Matcher;
import bgu.cs.util.Matcher.Case;
import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseInvoke;
import bgu.cs.util.soot.CaseReturnStmt;
import bgu.cs.util.soot.CaseReturnVoidStmt;
import flyClasses.Example;
import flyClasses.Trace;
import soot.ArrayType;
import soot.RefType;
import soot.SootClass;
import soot.SootMethod;
import soot.Type;
import soot.Unit;
import soot.Value;

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
	
	public static boolean isTempVar(Value var) {
		String varName = var.toString();
		return varName.equals(MyBodyTransformer.MY_PRIMITIVE_LOCAL_NAME)
				|| varName.equals(MyBodyTransformer.MY_REF_LOCAL_NAME);
	}
	
	public static boolean shouldIgnoreLocal(Value val) {
		return isTempVar(val) || !isPrimitive(val);
//		return isTempVar(val);
	}
	
	public static boolean shouldIgnoreUnit(Unit unit) {
		Case<Unit> c = commandMatcher.match(unit);
		if (isAssignStmt(c)) 
			return shouldIgnoreLocal(((CaseAssign)c).lhs);
		else if (isInvokeStmt(c)) return false;
		else if (isReturnStmt(c)) return false;
		else return true;
	}
	
	public static boolean isPrimitive(Value val) {
		Type valType = val.getType();
		return !(valType instanceof RefType || valType instanceof ArrayType);
	}
	
	public static boolean isObject(Type type) {
		return type instanceof RefType;
	}
	
	public static RefType asObject(Object val) {
		return (RefType) val;
	}
	
	public static Case<Unit> MatchUnit(Unit unit) {
		return commandMatcher.match(unit);
	}
}
