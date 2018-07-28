package flyClasses;

public class Trace {
	public static final String CLASS_NAME = "flyClasses.Trace";
	public static String UPDATE_ASSIGNMENT_PRIMITIVE_METHOD, UPDATE_ASSIGNMENT_OBJECT_METHOD, UPDATE_INVOKE_METHOD, UPDATE_RETURN_METHOD;
	
	static {
		UPDATE_ASSIGNMENT_PRIMITIVE_METHOD = "UpdateAssignmentPrimitive";
		UPDATE_ASSIGNMENT_OBJECT_METHOD = "UpdateAssignmentObject";
		UPDATE_INVOKE_METHOD = "UpdateInvoke";
		UPDATE_RETURN_METHOD = "UpdateReturn";
	}
	
	public static void UpdateAssignmentPrimitive(String varName, int val) {
		System.out.printf("%s <- %s\n", varName, val);
	}
	
	public static void UpdateAssignmentObject(String varName, Object val) {
		System.out.printf("%s <- %s\n", varName, val);
	}
	
	public static void UpdateInvoke() {
		System.out.println("invoked method");
	}
	
	public static void UpdateReturn() {
		System.out.println("returning...");
	}
}
