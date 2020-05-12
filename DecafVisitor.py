# Generated from Decaf.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete generic visitor for a parse tree produced by DecafParser.

class DecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DecafParser#program.
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#int_litereal.
    def visitInt_litereal(self, ctx:DecafParser.Int_literealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#bool_literal.
    def visitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#assign_op.
    def visitAssign_op(self, ctx:DecafParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#literal.
    def visitLiteral(self, ctx:DecafParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#airth_op.
    def visitAirth_op(self, ctx:DecafParser.Airth_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#rel_op.
    def visitRel_op(self, ctx:DecafParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#eq_op.
    def visitEq_op(self, ctx:DecafParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cond_op.
    def visitCond_op(self, ctx:DecafParser.Cond_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#id.
    def visitId(self, ctx:DecafParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_name.
    def visitMethod_name(self, ctx:DecafParser.Method_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#feild_name.
    def visitFeild_name(self, ctx:DecafParser.Feild_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#field_type.
    def visitField_type(self, ctx:DecafParser.Field_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#feild_decal.
    def visitFeild_decal(self, ctx:DecafParser.Feild_decalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx:DecafParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#bin_op.
    def visitBin_op(self, ctx:DecafParser.Bin_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#callout_arg.
    def visitCallout_arg(self, ctx:DecafParser.Callout_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#expr.
    def visitExpr(self, ctx:DecafParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_call.
    def visitMethod_call(self, ctx:DecafParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#var_name.
    def visitVar_name(self, ctx:DecafParser.Var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#var_type.
    def visitVar_type(self, ctx:DecafParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#var_value.
    def visitVar_value(self, ctx:DecafParser.Var_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#var_decal.
    def visitVar_decal(self, ctx:DecafParser.Var_decalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_params.
    def visitMethod_params(self, ctx:DecafParser.Method_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_type.
    def visitMethod_type(self, ctx:DecafParser.Method_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_param_type.
    def visitMethod_param_type(self, ctx:DecafParser.Method_param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_Param_names.
    def visitMethod_Param_names(self, ctx:DecafParser.Method_Param_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#method_decl.
    def visitMethod_decl(self, ctx:DecafParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#breaknCon.
    def visitBreaknCon(self, ctx:DecafParser.BreaknConContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#statement.
    def visitStatement(self, ctx:DecafParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx:DecafParser.BlockContext):
        return self.visitChildren(ctx)



del DecafParser