package flyClasses;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Example {
	public static final String CLASS_NAME = "flyClasses.Example";
	private String functionName;
	private List<String> stateReports;
	private Map<String, Object> locals;
	
	public Example(String functionName) {
		this.functionName = functionName;
		this.stateReports = new LinkedList<>();
		locals = new HashMap<>();
	}
	
	public void addLine(String line) {
		this.stateReports.add(line);
	}
	
	public void InitLocal(String name, boolean isPrimitive) {
		locals.put(name, isPrimitive ? 0 : null);
	}
	
	private static String getEqualityString(String var, Object val) {
		return String.format("%s == %s", var, val);
	}
	
	public void ReportState() {
		List<String> stateLines = new LinkedList<>();
		for (String localName : locals.keySet()) stateLines.add(getEqualityString(localName, locals.get(localName)));
		addLine(String.format("[%s]", String.join(" && ", stateLines)));
	}

	public void UpdateAssignmentPrimitive(String varName, int val) {
		locals.put(varName, val);
		ReportState();
	}

	public void UpdateAssignmentObject(String varName, Object val) {
		locals.put(varName, val);
		ReportState();
	}

	public void UpdateInvoke(String methodName) {
//		addLine(String.format("%s", methodName));
		
		// nothing to do here either, apparently
	}

	public void UpdateReturn() {
		// nothing to do here, apparently
	}
	
	public String getFunctionName() {
		return this.functionName;
	}
	
	public String getExampleText() {
		return String.format("example {\n\t%s\n}", String.join(" ->\n\t", stateReports));
	}
}
