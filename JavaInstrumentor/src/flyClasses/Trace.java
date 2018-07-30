package flyClasses;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Stack;

public class Trace {
	public static final String CLASS_NAME = "flyClasses.Trace";
	
	public static String 
	UPDATE_ASSIGNMENT_PRIMITIVE_METHOD, 
	UPDATE_ASSIGNMENT_OBJECT_METHOD, 
	UPDATE_INVOKE_METHOD, 
	UPDATE_RETURN_METHOD,
	INIT_EXAMPLE_METHOD,
	INIT_LOCAL_METHOD,
	FINISHED_INIT_LOCALS_METHOD,
	FINISH_METHOD,
	DEF_TYPES_METHOD;
	
	
	static String types = null;
	static Map<String, List<Example>> methodsExamples;
	static Stack<Example> workingExamples;
	
	static {
		UPDATE_ASSIGNMENT_PRIMITIVE_METHOD = "UpdateAssignmentPrimitive";
		UPDATE_ASSIGNMENT_OBJECT_METHOD = "UpdateAssignmentObject";
		UPDATE_INVOKE_METHOD = "UpdateInvoke";
		UPDATE_RETURN_METHOD = "UpdateReturn";
		INIT_EXAMPLE_METHOD = "newExample";
		INIT_LOCAL_METHOD = "InitLocal";
		FINISHED_INIT_LOCALS_METHOD = "FinishedInitLocals";
		FINISH_METHOD = "Finish";
		DEF_TYPES_METHOD = "defTypes";
		
		methodsExamples = new HashMap<>();
		workingExamples = new Stack<>();
	}
	
	public static void addSample(String sample) {
		System.out.printf("\t%s", sample);
	}
	
	public static void newExample(String functionName) {
		methodsExamples.putIfAbsent(functionName, new LinkedList<>());
		workingExamples.push(new Example(functionName));
	}
	
	public static void defTypes(String typesString) {
		types = typesString;
	}
	
	public static void InitLocal(String name, boolean isPrimitive) {
		workingExamples.peek().InitLocal(name, isPrimitive);;
	}
	
	public static void FinishedInitLocals() {
		workingExamples.peek().ReportState();
	}
	
	public static void Finish() {
		for (String key : methodsExamples.keySet()) {
			System.out.println(types);
			
			System.out.printf("%s {\n", key);
			
			for (Example e : methodsExamples.get(key)) {
				System.out.printf("\t%s\n", e.getExampleText().replaceAll("\n", "\n\t"));
			}
			System.out.println("}");
		}
	}
	
	public static void UpdateAssignmentPrimitive(String varName, int val) {
		workingExamples.peek().UpdateAssignmentPrimitive(varName, val);
	}
	
	public static void UpdateAssignmentObject(String varName, Object val) {
		workingExamples.peek().UpdateAssignmentObject(varName, val);
	}
	
	public static void UpdateInvoke(String methodName) {
		workingExamples.peek().UpdateInvoke(methodName);
	}
	
	public static void UpdateReturn() {
		Example e = workingExamples.pop();
		e.UpdateReturn();
		methodsExamples.get(e.getFunctionName()).add(e);
	}
}
