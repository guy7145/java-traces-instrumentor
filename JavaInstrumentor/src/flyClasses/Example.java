package flyClasses;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Example {
	public static final String CLASS_NAME = "flyClasses.Example";
	private String functionSignature;
	private List<String> stateReports;
	private Map<String, Object> locals;
	
	public Example(String functionSignature) {
		this.functionSignature = functionSignature;
		this.stateReports = new LinkedList<>();
		locals = new HashMap<>();
	}
	
	public void addLine(String line) {
		this.stateReports.add(line);
	}
	
	public void InitLocalDefault(String name, boolean isPrimitive) {
		locals.put(name, isPrimitive ? 0 : null);
	}
	
	public void InitLocal(String name, Object val) {
		locals.put(name, val);
	}
	
	private static String getEqualityString(String var, Object val) {
		return String.format("%s == %s", var, val);
	}
	
	public void ReportState() {
		List<String> stateEqualities = new LinkedList<>();
		for (String localName : locals.keySet()) stateEqualities.add(getEqualityString(localName, locals.get(localName)));
		addLine(String.format("[%s]", String.join(" && ", stateEqualities)));
	}

	public void UpdateAssignmentPrimitive(String varName, int val, boolean deltaOnly) {
		locals.put(varName, val);
		if (deltaOnly)
			addLine(String.format("[%s]", getEqualityString(varName, val)));
		else 
			ReportState();
	}

	public void UpdateAssignmentObject(String varName, Object val) {
		locals.put(varName, val);
		ReportState();
	}
	
	public void UpdateAssignmentStatement(String lval, String rval) {
		addLine(String.format("%s = %s;", lval, rval));
	}

	public void UpdateInvoke(String methodName) {
		addLine(String.format("%s", methodName)); // report invocation
	}

	public void UpdateReturn() {
		// nothing to do here, apparently
	}
	
	public String getFunctionSignature() {
		return this.functionSignature;
	}
	
	public String getExampleText() {
		return String.format("example {\n\t%s\n}", String.join("\n\t-> ", stateReports));
	}
}
