import bgu.cs.util.soot.CaseAssign;
import bgu.cs.util.soot.CaseAssignLocal_BinopExpr;
import bgu.cs.util.soot.CaseInvoke;
import flyClasses.Trace;
import soot.PatchingChain;
import soot.SootMethod;
import soot.Unit;
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
	
	private boolean reportInvokes;
	
	public UnitBodyTransformer(String[] userClasses, boolean deltaOnly, boolean reportInvokes) {
		super(userClasses, deltaOnly, reportInvokes);
	}
	
	@Override
	protected void patchAssignment(Unit patchedUnit, SootMethod method, CaseAssign assignment) {
		String rval;
		if (assignment instanceof CaseAssignLocal_BinopExpr) {
			BinopExpr bin_op = (BinopExpr)assignment.rhs;
			
			rval = getVariableName(bin_op.getOp1()) + bin_op.getSymbol() + getVariableName(bin_op.getOp2());
		}
		else rval = getVariableName(assignment.rhs);
		
		Stmt updateAssignStmt = Jimple.v().newInvokeStmt(
				Jimple.v().newStaticInvokeExpr(
						updateAssignStmtMethod.makeRef(), 
						StringConstant.v(getVariableName(assignment.lhs).toString()),
						StringConstant.v(rval)
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
