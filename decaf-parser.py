import antlr4 as ant
from DecafLexer import DecafLexer
from DecafVisitor import DecafVisitor
from DecafParser import DecafParser

class DecafPrintVisitor(DecafVisitor):
    def __init__(self):
        super().__init__()
        self.text = ''

    def printNode(self, ctx):
        self.text = self.text + '{\"name\": \"' + parser.ruleNames[ctx.getRuleIndex()] + '\",' + '\"value\":2,' + '\"children\":['
        self.visitChildren(ctx)
        self.text = self.text + ']},'
    
    def visitTerminal(self, ctx):
        self.text = self.text + '{\"name\": \"' + ctx.getText().replace('\\', '\\\\').replace('\"', '\\\"') + '\"},'
    
        
       # Visit a parse tree produced by DecafParser#program.
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        self.printNode(ctx)
        

    # Visit a parse tree produced by DecafParser#int_litereal.
    def visitInt_litereal(self, ctx:DecafParser.Int_literealContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#bool_literal.
    def visitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#assign_op.
    def visitAssign_op(self, ctx:DecafParser.Assign_opContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#literal.
    def visitLiteral(self, ctx:DecafParser.LiteralContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#airth_op.
    def visitAirth_op(self, ctx:DecafParser.Airth_opContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#rel_op.
    def visitRel_op(self, ctx:DecafParser.Rel_opContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#eq_op.
    def visitEq_op(self, ctx:DecafParser.Eq_opContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#cond_op.
    def visitCond_op(self, ctx:DecafParser.Cond_opContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#feild_name.
    def visitFeild_name(self, ctx:DecafParser.Feild_nameContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#feild_decal.
    def visitFeild_decal(self, ctx:DecafParser.Feild_decalContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx:DecafParser.LocationContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#bin_op.
    def visitBin_op(self, ctx:DecafParser.Bin_opContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#callout_arg.
    def visitCallout_arg(self, ctx:DecafParser.Callout_argContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#expr.
    def visitExpr(self, ctx:DecafParser.ExprContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#method_call.
    def visitMethod_call(self, ctx:DecafParser.Method_callContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#var_name.
    def visitVar_name(self, ctx:DecafParser.Var_nameContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#var_decal.
    def visitVar_decal(self, ctx:DecafParser.Var_decalContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#method_params.
    def visitMethod_params(self, ctx:DecafParser.Method_paramsContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#method_decl.
    def visitMethod_decl(self, ctx:DecafParser.Method_declContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#statement.
    def visitStatement(self, ctx:DecafParser.StatementContext):
        self.printNode(ctx)


    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx:DecafParser.BlockContext):
        self.printNode(ctx)

 
filein = open('testdata/parser/illegal-02', 'r')

lexer = DecafLexer(ant.InputStream(filein.read()))

stream = ant.CommonTokenStream(lexer)
parser = DecafParser(stream)
tree = parser.program()

visitor = DecafPrintVisitor()
visitor.visit(tree)
print(visitor.text)

