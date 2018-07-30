import soot.*;
import soot.options.Options;

import java.io.File;
import java.io.IOException;
import java.lang.ProcessBuilder.Redirect;
import java.util.Arrays;

import fj.data.Array;
import flyClasses.Example;
import flyClasses.Trace;

/**
 * Created by mian on 6/22/16.
 * https://www.sable.mcgill.ca/soot/tutorial/   More on profiling
 * argument example: TestInvoke
 */
public class EntryPoint {
	public static boolean flag_delta, flag_jimple, flag_main_found;
	public static String mainClass;
	public static final String 
	FLAG_DELTA = "--delta-only", 
	FLAG_JIMPLE = "--jimple",
	FLAG_MAIN = "--main";
	
	public static boolean verifyArguments(String[] args) {
		return args.length >= 2 && (flag_main_found || flag_jimple);
	}
	
	public static void printUsage() {
		System.out.printf("usage: java EntryPoint [options] [classes...]\n", FLAG_MAIN);
		
		System.out.println();
		System.out.println("[options]:");
		System.out.printf("%s \t\tonly output as jimple\n", FLAG_JIMPLE);
		System.out.printf("%s \t\tshow delta only\n", FLAG_DELTA);
		System.out.printf("%s <classname>\tthe class containing \"void main(String[] args)\" to run after execution\n", FLAG_MAIN);
		
		System.out.println();
		System.out.println("[classes...]:");
		System.out.println("names of classes to analyze (not including the main class)");
	}
	
	public static String[] readArgs(String[] args) {
		flag_delta = false;
		flag_jimple = false;
		flag_main_found = false;
		
		int lastFlagArg = 0;
		boolean updateLastFlagArgs;
		for(int i = 0; i < args.length; i++) {
			updateLastFlagArgs = true;
			
			if(args[i].equals(FLAG_DELTA)) flag_delta = true;
			else if (args[i].equals(FLAG_JIMPLE)) flag_jimple = true;
			else if (args[i].equals(FLAG_MAIN)) {
				i++;
				mainClass = args[i];
				flag_main_found = true;
			}
			else updateLastFlagArgs = false;
			
			if (updateLastFlagArgs) lastFlagArg = i;
		}
		
		if (!verifyArguments(args)) {
			printUsage();
			System.exit(0);
		}
		
		String[] extraClasses = Arrays.copyOfRange(args, lastFlagArg + 1, args.length);
		return extraClasses;
	}

	private static void printArgs(String[] extraClasses) {
		System.out.println("ARGUMENTS:");
		
		if (flag_jimple) System.out.println("using jimple output");
		if (flag_delta) System.out.println("showing delta only");
		
		System.out.printf("main class is %s\n", mainClass);
		
		if (extraClasses.length == 0) System.out.println("no extra classes");
		else {
			System.out.println("extra classes:");
			for (String s : extraClasses) System.out.println(s);
		}
		
		System.out.println();
		System.out.println("end of arguments.");
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
	
	public static String[] generateSootArgs(String[] args, String[] classNames) {
		String[] basicArgs = new String[] {
				"-output-format", 
				flag_jimple ? "jimple" : "class",
				Trace.CLASS_NAME,
				Example.CLASS_NAME,
				mainClass
		};
		
		String[] sootArgs = Arrays.copyOfRange(basicArgs, 0, basicArgs.length + classNames.length);
		for (int i = 0; i < classNames.length; i++) sootArgs[basicArgs.length + i] = classNames[i];
		return sootArgs;
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
		String[] extraClasses = readArgs(args);
		printArgs(extraClasses);
		System.out.println(String.join(" ", generateSootArgs(args, extraClasses)));
		setSootClassPath();
		setJimpleInstrumenter();
		soot.Main.main(generateSootArgs(args, extraClasses));
		if (!flag_jimple) runInstrumentedClass(mainClass);
	}
}
