import soot.*;
import soot.options.Options;

import java.io.File;
import java.io.IOException;
import java.lang.ProcessBuilder.Redirect;
import java.util.Arrays;

import flyClasses.MyCounter;
import flyClasses.Trace;

/**
 * Created by mian on 6/22/16.
 * https://www.sable.mcgill.ca/soot/tutorial/   More on profiling
 * argument example: TestInvoke
 */
public class EntryPoint {
	public static boolean flag_delta, flag_debug;
	public static final String FLAG_DELTA = "--delta", FLAG_DEBUG = "--debug";
	
	public static boolean verifyArguments(String[] args) {
		return args.length >= 1;
	}
	
	public static void printUsage() {
		System.err.println("usage: java EntryPoint classname <options...>");
		System.err.printf("%s toggle debug mode", FLAG_DEBUG);
		System.err.printf("%s trace delta", FLAG_DELTA);
	}
	
	public static String readArgs(String[] args) {
		flag_delta = false;
		flag_debug = false;
		
		if (!verifyArguments(args)) {
			printUsage();
			System.exit(0);
		}
		
		for(int i = 0; i < args.length; i++) {
			if(args[i].equals(FLAG_DELTA)) flag_delta = true;
			else if (args[i].equals(FLAG_DEBUG)) flag_debug = true;
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
	
	public static void setJimpleInstrumenter() {
		final String JIMPLE_TRANSFORMATION_PACK = "jtp";
		Pack jtp = PackManager.v().getPack(JIMPLE_TRANSFORMATION_PACK);
		jtp.add(new Transform("jtp.instrumentation-phsae", new MyBodyTransformer()));
	}
	
	public static String[] generateSootArgs(String classNameArg) {
		return new String[] {
				classNameArg,
				MyCounter.CLASS_NAME,
				Trace.CLASS_NAME,
//				"-w", // toggle whole-program mode
//				"-output-format", 
//				"jimple",
		};
	}
	
	public static void runInstrumentedClass(String className) {
		String[] command = new String[] {"java", className};
		String sootOutputPath = System.getProperty("user.dir") + "\\sootOutput";
		
		ProcessBuilder builder = 
				new ProcessBuilder(command)
				.directory(new File(sootOutputPath))
				.redirectOutput(Redirect.INHERIT)
				.redirectError(Redirect.INHERIT);
		
		try { 
			System.out.printf("output of the instrumented \"%s\":\n", className);
			Process p = builder.start();
		} catch (IOException e) {
			e.printStackTrace();
			System.out.println("failed to start instrumented class with java");
		}
	}
	
	public static void main(String[] args) {
		String className = readArgs(args);
		
		setSootClassPath();
		setJimpleInstrumenter();
		soot.Main.main(generateSootArgs(className));
		
		runInstrumentedClass(className);
	}
}
