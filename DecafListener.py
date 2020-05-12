# Generated from Decaf.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#program.
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafParser#program.
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafParser#int_litereal.
    def enterInt_litereal(self, ctx:DecafParser.Int_literealContext):
        pass

    # Exit a parse tree produced by DecafParser#int_litereal.
    def exitInt_litereal(self, ctx:DecafParser.Int_literealContext):
        pass


    # Enter a parse tree produced by DecafParser#bool_literal.
    def enterBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#bool_literal.
    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#assign_op.
    def enterAssign_op(self, ctx:DecafParser.Assign_opContext):
        pass

    # Exit a parse tree produced by DecafParser#assign_op.
    def exitAssign_op(self, ctx:DecafParser.Assign_opContext):
        pass


    # Enter a parse tree produced by DecafParser#literal.
    def enterLiteral(self, ctx:DecafParser.LiteralContext):
        pass

    # Exit a parse tree produced by DecafParser#literal.
    def exitLiteral(self, ctx:DecafParser.LiteralContext):
        pass


    # Enter a parse tree produced by DecafParser#airth_op.
    def enterAirth_op(self, ctx:DecafParser.Airth_opContext):
        pass

    # Exit a parse tree produced by DecafParser#airth_op.
    def exitAirth_op(self, ctx:DecafParser.Airth_opContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op.
    def enterRel_op(self, ctx:DecafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op.
    def exitRel_op(self, ctx:DecafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op.
    def enterEq_op(self, ctx:DecafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op.
    def exitEq_op(self, ctx:DecafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafParser#cond_op.
    def enterCond_op(self, ctx:DecafParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DecafParser#cond_op.
    def exitCond_op(self, ctx:DecafParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DecafParser#id.
    def enterId(self, ctx:DecafParser.IdContext):
        pass

    # Exit a parse tree produced by DecafParser#id.
    def exitId(self, ctx:DecafParser.IdContext):
        pass


    # Enter a parse tree produced by DecafParser#method_name.
    def enterMethod_name(self, ctx:DecafParser.Method_nameContext):
        pass

    # Exit a parse tree produced by DecafParser#method_name.
    def exitMethod_name(self, ctx:DecafParser.Method_nameContext):
        pass


    # Enter a parse tree produced by DecafParser#feild_name.
    def enterFeild_name(self, ctx:DecafParser.Feild_nameContext):
        pass

    # Exit a parse tree produced by DecafParser#feild_name.
    def exitFeild_name(self, ctx:DecafParser.Feild_nameContext):
        pass


    # Enter a parse tree produced by DecafParser#field_type.
    def enterField_type(self, ctx:DecafParser.Field_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#field_type.
    def exitField_type(self, ctx:DecafParser.Field_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#feild_decal.
    def enterFeild_decal(self, ctx:DecafParser.Feild_decalContext):
        pass

    # Exit a parse tree produced by DecafParser#feild_decal.
    def exitFeild_decal(self, ctx:DecafParser.Feild_decalContext):
        pass


    # Enter a parse tree produced by DecafParser#location.
    def enterLocation(self, ctx:DecafParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafParser#location.
    def exitLocation(self, ctx:DecafParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafParser#bin_op.
    def enterBin_op(self, ctx:DecafParser.Bin_opContext):
        pass

    # Exit a parse tree produced by DecafParser#bin_op.
    def exitBin_op(self, ctx:DecafParser.Bin_opContext):
        pass


    # Enter a parse tree produced by DecafParser#callout_arg.
    def enterCallout_arg(self, ctx:DecafParser.Callout_argContext):
        pass

    # Exit a parse tree produced by DecafParser#callout_arg.
    def exitCallout_arg(self, ctx:DecafParser.Callout_argContext):
        pass


    # Enter a parse tree produced by DecafParser#expr.
    def enterExpr(self, ctx:DecafParser.ExprContext):
        pass

    # Exit a parse tree produced by DecafParser#expr.
    def exitExpr(self, ctx:DecafParser.ExprContext):
        pass


    # Enter a parse tree produced by DecafParser#method_call.
    def enterMethod_call(self, ctx:DecafParser.Method_callContext):
        pass

    # Exit a parse tree produced by DecafParser#method_call.
    def exitMethod_call(self, ctx:DecafParser.Method_callContext):
        pass


    # Enter a parse tree produced by DecafParser#var_name.
    def enterVar_name(self, ctx:DecafParser.Var_nameContext):
        pass

    # Exit a parse tree produced by DecafParser#var_name.
    def exitVar_name(self, ctx:DecafParser.Var_nameContext):
        pass


    # Enter a parse tree produced by DecafParser#var_type.
    def enterVar_type(self, ctx:DecafParser.Var_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#var_type.
    def exitVar_type(self, ctx:DecafParser.Var_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#var_value.
    def enterVar_value(self, ctx:DecafParser.Var_valueContext):
        pass

    # Exit a parse tree produced by DecafParser#var_value.
    def exitVar_value(self, ctx:DecafParser.Var_valueContext):
        pass


    # Enter a parse tree produced by DecafParser#var_decal.
    def enterVar_decal(self, ctx:DecafParser.Var_decalContext):
        pass

    # Exit a parse tree produced by DecafParser#var_decal.
    def exitVar_decal(self, ctx:DecafParser.Var_decalContext):
        pass


    # Enter a parse tree produced by DecafParser#method_params.
    def enterMethod_params(self, ctx:DecafParser.Method_paramsContext):
        pass

    # Exit a parse tree produced by DecafParser#method_params.
    def exitMethod_params(self, ctx:DecafParser.Method_paramsContext):
        pass


    # Enter a parse tree produced by DecafParser#method_type.
    def enterMethod_type(self, ctx:DecafParser.Method_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#method_type.
    def exitMethod_type(self, ctx:DecafParser.Method_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#method_param_type.
    def enterMethod_param_type(self, ctx:DecafParser.Method_param_typeContext):
        pass

    # Exit a parse tree produced by DecafParser#method_param_type.
    def exitMethod_param_type(self, ctx:DecafParser.Method_param_typeContext):
        pass


    # Enter a parse tree produced by DecafParser#method_Param_names.
    def enterMethod_Param_names(self, ctx:DecafParser.Method_Param_namesContext):
        pass

    # Exit a parse tree produced by DecafParser#method_Param_names.
    def exitMethod_Param_names(self, ctx:DecafParser.Method_Param_namesContext):
        pass


    # Enter a parse tree produced by DecafParser#method_decl.
    def enterMethod_decl(self, ctx:DecafParser.Method_declContext):
        pass

    # Exit a parse tree produced by DecafParser#method_decl.
    def exitMethod_decl(self, ctx:DecafParser.Method_declContext):
        pass


    # Enter a parse tree produced by DecafParser#breaknCon.
    def enterBreaknCon(self, ctx:DecafParser.BreaknConContext):
        pass

    # Exit a parse tree produced by DecafParser#breaknCon.
    def exitBreaknCon(self, ctx:DecafParser.BreaknConContext):
        pass


    # Enter a parse tree produced by DecafParser#statement.
    def enterStatement(self, ctx:DecafParser.StatementContext):
        pass

    # Exit a parse tree produced by DecafParser#statement.
    def exitStatement(self, ctx:DecafParser.StatementContext):
        pass


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass


