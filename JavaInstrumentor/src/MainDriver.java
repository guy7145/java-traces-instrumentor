import soot.*;
import soot.options.Options;

import java.io.File;
import java.util.Arrays;

import flyClasses.MyCounter;

/**
 * Created by mian on 6/22/16.
 * https://www.sable.mcgill.ca/soot/tutorial/   More on profiling
 * argument example: TestInvoke
 */
public class MainDriver {
	public static boolean flag_delta, flag_debug;
	public static final String FLAG_DELTA = "--delta", FLAG_DEBUG = "--debug";
	
	public static boolean verifyArguments(String[] args) {
		return true;
	}
	
	public static void printUsage() {
		System.err.println("Usage: java MainDriver classname [options]");
		System.err.println("options:");
		System.err.println("-d : trace delta");
	}
	
	public static String readArgs(String[] args) {
		flag_delta = false;
		flag_debug = false;
		
		if (!verifyArguments(args)) {
			printUsage();
			System.exit(0);
		}
		
		for(int i = 0; i < args.length; i++) {
			
			if(args[i].equals(FLAG_DELTA))
				flag_delta = true;
			
			else if (args[i].equals(FLAG_DEBUG))
				flag_debug = true;
		
		}
		
		if (flag_debug) {
			System.out.println("debug mode on");
			
			if (flag_delta) System.out.println("delta flag on");
		}
		
		return args[0];
	}
	
	public static void setSootClassPath() {
		StringBuilder classpaths = new StringBuilder();
		
		classpaths.append(Scene.v().getSootClassPath());
		classpaths.append(";bin");
		
		Scene.v().setSootClassPath(classpaths.toString());
	}
	
	public static String[] generateSootArgs(String classNameArg) {
		return new String[] {
				classNameArg,
				"flyClasses.MyCounter",
				"-output-format", 
				"jimple"
		};
	}
	
	public static void runResultsClass(String className) {
		String sootOutputPath = System.getProperty("user.dir") + "\\sootOutput";
		System.out.println(sootOutputPath);
		
	}
	
	public static void main(String[] args) {
		setSootClassPath();
		String className = readArgs(args);

		Pack jtp = PackManager.v().getPack("jtp");
		jtp.add(new Transform("jtp.instrumenter", new InvokeStaticInstrumenter()));
		
		soot.Main.main(generateSootArgs(className));
		runResultsClass(className);
	}
}
