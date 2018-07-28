package flyClasses;

public class Trace {
	public static final String CLASS_NAME = "flyClasses.Trace";
	public static String UPDATE_ASSIGNMENT_METHOD, UPDATE_INVOKE_METHOD, UPDATE_RETURN_METHOD;
	
	static {
		UPDATE_ASSIGNMENT_METHOD = "UpdateAssignment";
		UPDATE_INVOKE_METHOD = "UpdateInvoke";
		UPDATE_RETURN_METHOD = "UpdateReturn";
	}
	
	public static void UpdateAssignment(String varName, Object val) {
		System.out.printf("%s <- %s\n", varName, val);
	}
	
	public static void UpdateInvoke() {
		System.out.println("invoked method");
	}
	
	public static void UpdateReturn() {
		System.out.println("returning...");
	}
}
