import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseAssignLocal_BinopExpr;
import bgu.cs.util.soot.CaseInvoke;
import flyClasses.Trace;
import soot.PatchingChain;
import soot.SootMethod;
import soot.Unit;
import soot.Value;
import soot.jimple.BinopExpr;
import soot.jimple.InvokeExpr;
import soot.jimple.Jimple;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;
import soot.jimple.internal.AbstractBinopExpr;


public class UnitBodyTransformer extends MyBodyTransformer {
	
	static SootMethod updateAssignStmtMethod;
	
	static {
		updateAssignStmtMethod = MyBodyTransformer.traceClass.getMethodByName(Trace.UPDATE_ASSIGNMENT_STMT_METHOD);
	}
	
	public UnitBodyTransformer(String[] userClasses, boolean deltaOnly, boolean reportInvokes) {
		super(userClasses, deltaOnly, reportInvokes);
	}
	
	@Override
	protected void patchAssignment(Unit patchedUnit, SootMethod method, CaseAssign assignment) {
		Value rval = getRValJMinor(assignment);
		
		Stmt updateAssignStmt = Jimple.v().newInvokeStmt(
				Jimple.v().newStaticInvokeExpr(
						updateAssignStmtMethod.makeRef(), 
						StringConstant.v(getVariableName(assignment.lhs)),
						rval
						)
				);
		
		method.getActiveBody().getUnits().insertAfter(updateAssignStmt, patchedUnit);
	}
	
	@Override
	protected void patchInvoke(Unit patchedUnit, PatchingChain<Unit> methodUnits, CaseInvoke invocation) {
		Stmt updateInvokeStmt = Jimple.v().newInvokeStmt(
				Jimple.v().newStaticInvokeExpr(
						updateInvoke.makeRef(), 
						StringConstant.v(invocation.invoke.toString())
						)
				);
		
		methodUnits.insertAfter(updateInvokeStmt, patchedUnit);
	}
}
