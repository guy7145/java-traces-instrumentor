package flyClasses;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
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
	UPDATE_ASSIGNMENT_STMT_METHOD,
	UPDATE_INVOKE_METHOD, 
	UPDATE_RETURN_METHOD,
	INIT_EXAMPLE_METHOD,
	INIT_LOCAL_OBJECT_METHOD,
	INIT_LOCAL_PRIMITIVE_METHOD,
	INIT_LOCAL_DEFAULT_METHOD,
	FINISHED_INIT_LOCALS_METHOD,
	FINISH_METHOD,
	DEF_TYPES_METHOD,
	SET_DELTA_MODE_METHOD;
	
	
	static String types = null;
	static boolean deltaOnly = false;
	static Map<String, List<Example>> methodsExamples;
	static Stack<Example> workingExamples;
	
	static {
		UPDATE_ASSIGNMENT_PRIMITIVE_METHOD = "UpdateAssignmentPrimitive";
		UPDATE_ASSIGNMENT_OBJECT_METHOD = "UpdateAssignmentObject";
		UPDATE_ASSIGNMENT_STMT_METHOD = "UpdateAssignmentStatement";
		UPDATE_INVOKE_METHOD = "UpdateInvoke";
		UPDATE_RETURN_METHOD = "UpdateReturn";
		INIT_EXAMPLE_METHOD = "newExample";
		INIT_LOCAL_OBJECT_METHOD = "InitLocalObject";
		INIT_LOCAL_PRIMITIVE_METHOD = "InitLocalInt";
		INIT_LOCAL_DEFAULT_METHOD = "InitLocalDefault";
		FINISHED_INIT_LOCALS_METHOD = "FinishedInitLocals";
		FINISH_METHOD = "Finish";
		DEF_TYPES_METHOD = "defTypes";
		SET_DELTA_MODE_METHOD = "setDeltaMode";
		
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
	
	public static void setDeltaMode(boolean deltaOnly) {
		Trace.deltaOnly = deltaOnly;
	}
	
	public static void InitLocalDefault(String name, boolean isPrimitive) {
		workingExamples.peek().InitLocalDefault(name, isPrimitive);;
	}
	
	public static void InitLocalObject(String name, Object val) {
		workingExamples.peek().InitLocal(name, val);
	}
	
	public static void InitLocalInt(String name, int val) {
		InitLocalObject(name, val);
	}
	
	public static void FinishedInitLocals() {
		workingExamples.peek().ReportState();
	}
	
	public static void Finish() {
		for (String method : methodsExamples.keySet()) {
			String filename = method.substring(0, method.indexOf("(")) + ".spec";
			try {
				File file = new File(filename);
				if (file.exists()) file.delete();
				
				FileWriter fw = new FileWriter(file);
				
				fw.write(types);
				
				fw.write(String.format("%s {\n", method));
				
				for (Example e : methodsExamples.get(method)) 
					fw.write(String.format("\t%s\n", e.getExampleText().replaceAll("\n", "\n\t")));
				
				fw.write("}");
				fw.close();
				
			} catch (IOException e1) {
				System.out.printf("failed to write method spec file: %s\n", filename);
				e1.printStackTrace();
				
			}
		}
	}
	
	public static void UpdateAssignmentPrimitive(String varName, int val) {
		workingExamples.peek().UpdateAssignmentPrimitive(varName, val, deltaOnly);
	}
	
	public static void UpdateAssignmentObject(String varName, Object val) {
		workingExamples.peek().UpdateAssignmentObject(varName, val, deltaOnly);
	}
	
	public static void UpdateAssignmentStatement(String lval, String rval) {
		workingExamples.peek().UpdateAssignmentStatement(lval, rval);
	}
	
	public static void UpdateInvoke(String methodName) {
		workingExamples.peek().UpdateInvoke(methodName);
	}
	
	public static void UpdateReturn() {
		Example e = workingExamples.pop();
		e.UpdateReturn();
		methodsExamples.get(e.getFunctionSignature()).add(e);
	}
}
