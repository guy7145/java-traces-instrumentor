package flyClasses;
import java.util.HashMap;
import java.util.Map;

public class Scope {
	public static final String CLASS_NAME = "flyClasses.Scope";
	
	/*  
	 * 
	 *    r1
	 * -> r2 -> val, scope -> next 
	 *    r3
	 * 
	 */
	
	
	Object val;
	Scope currentValScope;
	Map<String, Scope> innerScopes;
	
	public Scope() {
		val = null;
		resetScope();
	}
	
	private void resetScope() {
		innerScopes = new HashMap<String, Scope>();
	}
	
	private void setVal(Object val) {
		this.val = val;
		resetScope();
	}
	
	private Object getVal() {
		return val;
	}
	
	public void set(String name, Object val) {		
		Scope s = this.getScope(name);
		s.setVal(val);
	}
	
	private Scope getScope(String name) {
		String[] names = name.split(".");
		Scope s = this;
		for (int i = 0; i < names.length; i++)
			s = s.getScope(names[i]);
		return s;
	}
	
	public Object get(String name) {
		return getScope(name).getVal();
	}
}
