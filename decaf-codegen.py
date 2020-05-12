import os
import antlr4 as ant
from SymbolTable import VarSymbol, MethodSymbol
import SymbolTable 
os.system("java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Decaf.g4 -visitor")
# https://moodle.mmu.ac.uk/pluginfile.php/4161924/mod_resource/content/7/6G6Z1110%20Decaf%20Specification.pdf
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafVisitor import DecafVisitor


"""
code comments through out the file will be mostly using this multiline 
comment format, if you are using a dark mode on the spyder editor then 
it can be confusing to see between print statements or comments.

single line coments will still with a hash tag.

there are of course a few problems with the semantic chekcing below, there are the var_decal 
method, this method has checks all the semnatics fine but sadly it aware that they maybe some bugs 
that  still exisit wthin the code. 

there may also be some bugs in the semantic checkking for feild decal as it does not add the correct type 
to the symbol table.

there is also a problem with checking for break or continue outside of of a for loop as it ony works if there are no other 
statments inside of the method.

x86 asm code tested with an online complier.

in one test the parser throws an error but the semantic checking does not, I feel like if the parser prints an error
then the semantic checking does not need too.
"""
#check semantics and generate code
class DecafCodeGenVisitor(DecafVisitor):
    
    def __init__(self):
        super().__init__()
        #varibles used in code generation 
        self.body = 'global main\n'
        self.head = 'section .text\n'
        
        #varibles used in semanctic checking.
        self.st = SymbolTable.SymbolTable()
        self.params = []
        self.eq_op = None
        self.returnType = None
        self.breakncon =None
        self.text = None
    """
    visit the program node in the parse tree
    """
    def visitProgram(self, ctx:DecafParser.ProgramContext):      
        self.st.enterScope()
        self.text = ctx.getText()
        line_number = ctx.start.line
        """ 
        if there is main method in side the decaf code then add a main to the 
        ASM code else tell the user there is no main method in the code
        """
        if "main" in self.text: 
            self.body +=  "main:\n"
        else: 
            print("ERROR no main method found")      
            
        """
        check that a person is not using a break or continue outside of a for loop
        """
        self.visitChildren(ctx)
        for i in range(len(ctx.method_decl())):
            for j in range(len(ctx.method_decl(i).block().statement())): 
                #method_block = ctx.method_decl(i).block().getText()
                statments = ctx.method_decl(i).block().statement(j).getText()
                if "for" in statments: 
                    pass
                else:
                    if "break" in statments or "continue" in statments:
                        print("ERROR cannot use break or  continue outside of for loop. line:", line_number)    
        """
        add ret to the end of all code that is generated, this tells the ASM code where to end.  
        """
        self.body +="ret\n"
        self.st.exitScope()                
        
    #visit field decal     
    def visitFeild_decal(self, ctx:DecafParser.Feild_decalContext):
        """
        line_number is used in all further methods, it is used to get the line number which 
        something is written on
        """
        line_number = ctx.start.line
        Feildtype = ctx.field_type().getText()
        """get the id of the vield decal"""
        feildVarName = ctx.feild_name(0).id().getText()
        """get the field name to check if it already exisits"""
        VarName = ctx.feild_name(0)
            
        if self.st.probe(feildVarName) !=None: 
            print("ERROR: varible", "'"+feildVarName+"'", "decalred twice"," on line", line_number)
        else:
            """check if the var_name contains a [ is it does then it's a array varible """
            if "[" in VarName.getText():
                
                int_litereal = None
                for i in range(len(ctx.feild_name())):
                    int_litereal = ctx.feild_name(i).int_litereal()
        
                if int_litereal !=None:
                    int_litereal = int_litereal.getText()
                    """check  that the int litereal is bigger than zero"""
                    if int(int_litereal) > 0:
                        """if everything is samanticly valid add the array to the symbol table"""
                        Feild_decalsysmbol = VarSymbol(
                                id = VarName.id().getText(),
                                type = "array",
                                line = line_number,
                                size = 8,
                                mem = SymbolTable.HEAP
                                )
                        self.st.addSymbol(Feild_decalsysmbol)
                    else:
                        print("ERROR: arrays of length zero are not allowed" +", line", line_number)  
                
            else:
                Feild_decalsysmbol = VarSymbol(
                        id = feildVarName,
                        type = Feildtype,
                        line = line_number,
                        size = 8,
                        mem = SymbolTable.HEAP
                        )
                
                self.st.addSymbol(Feild_decalsysmbol)
        val = self.visitChildren(ctx)   
        feildVarNames = ctx.feild_name()
        """
        loop through the array of all feild decals and check if any of them have 
        already decalred by comparing the all of the field names againt each other
        """
        for i in range(len(feildVarNames)):
            for j in range(i + 1, len(feildVarNames)):
                if feildVarNames[i].getText() == feildVarNames[j].getText(): 
                    print("ERROR: varible", "'"+feildVarNames[i].getText()+"'", "decalred twice"," on line", line_number)
                else:
                    """if everything is valid add to symbol table"""
                    for k in feildVarNames:
                        Feild_decalsysmbol = VarSymbol(
                                id = k,
                                type = Feildtype,
                                line = line_number,
                                size = 8,
                                mem = SymbolTable.HEAP
                                )                
                        self.st.addSymbol(Feild_decalsysmbol)
        return val                
    
    def visitLocation(self, ctx:DecafParser.LocationContext):
        return self.visitChildren(ctx)         
        
    def visitStatement(self, ctx:DecafParser.StatementContext):
        line_number = ctx.start.line
        statmentName = ctx.location()
        
        if ctx.expr():
           #visit first expression 
           self.visit(ctx.expr(0))
           
           #move the stack pointer and save value of first expression
           self.st.stack_pointer[-1] += 8
           self.body += 'movq %rax, ' + str(-self.st.stack_pointer[-1]) + '(%rsp)\n'
            
           #visit second expression
           self.visit(ctx.expr(0))
           
           self.body += 'movq ' + str(-self.st.stack_pointer[-1]) + '(%rsp), %r10\n'
           self.st.stack_pointer[-1] -= 8
           self.body += 'movq %rax, %r11\n'
           
           
           
        
        """if a loction exists then assign the locaton varible to look on the symbol table"""
        if ctx.location():
            location = self.st.lookup(ctx.location().getText())
            
            if ctx.expr(): 
                expr = ctx.expr(0).expr(0)

                if expr.literal():
                    if self.st.lookup(location.id).type == "boolean":
                        try: 
                            """if the lookup if type returns a boolean then try to int the expression if that is possible throw an error"""
                            int(ctx.expr(0).expr(0).getText())
                            print("ERROR: cannot assign boolean to int, line number:", line_number)
                        except:
                            """if that fails it can be assumed that the opertor is wrong"""
                            print("ERROR cannot use that operator with booleans, line number:", line_number)
        
        if ctx.breaknCon() !=None:
            self.breakncon = ctx.breaknCon().getText()
        if ctx.FOR():
            """try and int the item in side of the for loop if that fails error"""
            for items in ctx.expr():
                 try: 
                     int(items.getText())
                 except:
                    if items.location() !=None:
                       if self.st.lookup(items.location().getText()).type !="int":
                           print("ERROR: type is not int. Line number:", line_number)
                    else:   
                        print("ERROR: type int must be used here in for loop. Line number:", line_number)
        """
        if an if statment exists then check  
        if the expression is an boolean
        
        check if you are comparing two things of the same types 
        """                 
        if ctx.IF() !=None:
            
            if ctx.expr(0).bin_op() == None: 
                if self.st.lookup(ctx.expr(0).getText()).type != "boolean": 
                    print("ERROR", "cannot evaluate type " +self.st.lookup(ctx.expr(0).getText()).type
                          + " to boolean, on line:", line_number)
            else:
                """get the eq operator """
                self.eq_op = ctx.expr(0).bin_op().eq_op().getText() 
                if ctx.expr(0).bin_op():
                    """get the bin op """
                    bin_op = ctx.expr(0).bin_op().getText()
                    
                    ids = ctx.expr(0).getText().replace(bin_op, "") 
                    """make a list out of all the ids"""
                    listOfIds = list(ids)
                    """compare the operands of of bin_op and if they are not the same type then error"""
                    if self.st.lookup(listOfIds[0]).type != self.st.lookup(listOfIds[1]).type:
                        print("cannot compare "+ self.st.lookup(listOfIds[0]).type + 
                              " with "+ self.st.lookup(listOfIds[1]).type+ " line number", line_number)
                else:
                    """if bin op is not found get the type of the expression and if it's not boolean, throw an error"""
                    if self.st.lookup(ctx.expr(0).getText()).type !="boolean": 
                        print("ERROR: "+"cannot evaluate type int line number", line_number)
                        
        if  self.eq_op !=None: 
            expression = ctx.expr(0).getText()
            ids = expression.replace(self.eq_op, "")
            idList = list(ids)
            """check if the operands logical and  or both boolean""" 
            if self.st.lookup(idList[0]).type and self.st.lookup(idList[1]).type != "boolean": 
                print("ERROR: cannot use logical not here. Line number:", line_number)
        expr = ctx.expr(0)
        expArrry =[]
        if expr !=None:
            if "+ " in expr.getText():
                """make an array of the epressions"""
                expArrry = expr.replace("+", ",")
                expArrry= expArrry.split(",")        
        var_name = None
        varnames = None
        for varnames in expArrry: 
            var_name = self.st.lookup(varnames)
            if var_name !=None: 
                pass
            else: 
                """error if symbol is on symbol table already"""
                print("ERROR: varible referanced but never assinged " + " '"+varnames+"' "+ "on line", line_number ) 
        if statmentName !=None:
            var_symbol = self.st.lookup(statmentName.getText())
            if var_symbol !=None: 
                pass
            else: 
               print("ERROR:", "varible referanced but never assinged","'",statmentName.getText()+"'","on line", line_number)                
        return self.visitChildren(ctx)    
    #visit method decal node in tree
    def visitMethod_decl(self, ctx:DecafParser.Method_declContext):
        
        self.params
        param_types = []
        ctx.method_param_type()
        #line used for debugging
        #print(ctx.method_param_type(0).getText()) 
        method_name= ctx.id(0).getText()
        return_type = ctx.method_type().getText()
        line_number = ctx.start.line
        
               
        for i in range(len(ctx.method_param_type())):
            param_types.append(ctx.method_param_type(i).getText())
            
        for i in range(len(ctx.method_Param_names())): 
            self.params.append(ctx.method_Param_names(i).getText())
        
        #line used for debugging
        #print(ctx.method_Param_names(0).getText())

        for i in range(len(param_types)):
            if self.params == []: 
                method_params = VarSymbol(
                        id   = self.params[i],
                        type = param_types[i],
                        line = line_number,
                        size = 8,
                        mem = SymbolTable.STACK                    
                        )
                self.st.addSymbol(method_params)
            else:             
                method_params = VarSymbol(
                        id   = self.params[i],
                        type = param_types[i],
                        line = line_number,
                        size = 8,
                        mem = SymbolTable.STACK                    
                        )
                self.st.addSymbol(method_params)
                
                method_symbol = MethodSymbol(
                        id   = method_name,
                        type = return_type,
                        line = line_number,
                        params = ctx.method_Param_names()
                        )
                self.st.addSymbol(method_symbol)
        if self.st.lookup(method_name) !=None:
            for i in range(len(self.st.lookup(method_name).params)):
            
                method_params = VarSymbol(
                        id   = ctx.method_Param_names(i).getText(),
                        type = ctx.method_param_type(i).getText(),
                        line = line_number,
                        size = 8,
                        mem = SymbolTable.STACK                    
                        )
                self.st.addSymbol(method_params)
           
        """don't add main to code more than once"""        
        if "main" in method_name:
            pass
        else:
            self.body+=method_name+":"+"\n"
        """get the statment in the return statment"""
        returnStatment = ctx.block().statement()
        if returnStatment !=None:
            for item in returnStatment:
                if "if" in item.getText():
                    pass
                elif "return" in item.getText():
                    if self.st.lookup(item.expr(0)) == None: 
                        """if return of method is void then throw and error""" 
                        if return_type == "void":
                            print("method on line:",line_number,"should not return anything")
                        elif return_type == "int": 
                            """try to int the expr, if that fails throw an error""" 
                            try: 
                                int(item.expr(0).getText())
                            except: 
                                print("ERROR: wrong return type found for method on line:", line_number)
                        elif self.st.lookup(item.expr(0).getText()).type !=return_type:     
                            print("ERROR: type of retrun statement does not match method return type, line number:", line_number)            
                        else: 
                            Addr = self.st.lookup(item.expr(0).getText()).getAddr() 
                        
                            self.st.stack_pointer[-1] += 8
                            self.body += 'movq %rax, ' + str(-self.st.stack_pointer[-1]) + '(%rsp)\n'
                            
                            self.body += "movq "+str(Addr)+ " (%rbp), "+" %rax"+"\n"""
                        
                        
                        
        if return_type == "int" and returnStatment == []:
            print("ERROR: method missing return statement", line_number)
        if return_type == "boolean" and returnStatment == []:
            print("ERROR: method missing return statement", line_number)    
        return self.visitChildren(ctx)
     # Visit a parse tree produced by DecafParser#method_call.
    def visitMethod_call(self, ctx:DecafParser.Method_callContext):
        
        line_number = ctx.start.line
        param_names = ctx.expr()
        if "callout" in ctx.getText(): 
            callout_argument = ctx.callout_arg(0).getText()
            print(callout_argument)
            self.body +=	'mov	edx, len \n' #message length
            self.body +=	'mov	ecx, msg \n' #message to to be written
            self.body +=	'mov	ebx, 1 \n' #file descriptor  
            self.body +=	'mov	eax, 4 \n'	 #system call number (system write)   
            self.body +=	'int	0x80 \n'  #call the kernel      
            self.body +=	'mov	eax, 1 \n'	#system call number (system exit)     
            self.body +=	'int	0x80 \n'     #call kernel again   
            self.body +=    'section .data \n'
            
            self.body += 'msg  db '+callout_argument+', 0x0'+'\n' #string to be printed
            self.body += 'len equ $-msg \n' #ength of string 
            
        else:
            method_params = self.st.lookup(ctx.id().getText()).params
            
            """
            if the length of the paramertor lists in the method call and 
            the original method decal are not the same throw an error
            """
            if len(method_params)  != len(param_names): 
                print("ERROR: "+"method "+ctx.id().getText()+" epecting",len(method_params),"input params but got",len(param_names),"on line",line_number) 
            else:
                for i in range(len(param_names)):
                    """
                    if any of the method params in the 
                    original method decal is a boolean
                    check if the types of the oringal params 
                    and the types of the called params match
                    """ 
                    if self.st.lookup(method_params[i].getText()).type == "boolean":
                          for i in range(len(ctx.expr())):
                             if self.st.lookup( param_names[i].getText()) !=None:
                                 if self.st.lookup( param_names[i].getText()).type != self.st.lookup(method_params[i].getText()).type:
                                     print("ERROR: wrong paramertor type found for method call on line:", line_number)
                          try: 
                             int(param_names[i].getText())
                             print("ERROR: parametor type cannot be boolean for method call", "int", "on line:", line_number)
                          except: 
                           pass
            
        """
        check if a varible inside of method call exists
        """
        if param_names !=None:
            for name in param_names:
                if name.literal() ==None: 
                    pass
                else:
                    if name.literal().bool_literal() or name.literal().int_litereal():
                        pass
                    else:
                        self.params.append(name.getText())
                        var_symbol = self.st.lookup(name.getText())
                        if var_symbol !=None: 
                            pass
                        else: 
                            print("ERROR:", "varible referanced but never assinged "+" '"+name.getText()+"' "+"on line",line_number)
        return self.params
        # Visit a parse tree produced by DecafParser#block."""
        return self.visitChildren(ctx)
    
   
    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx:DecafParser.BlockContext):
        return self.visitChildren(ctx)
        
    def visitVar_value(self, ctx:DecafParser.var_value):
        line_number = ctx.start.line
        ID = ctx.id()
        """
        if an id is within the var value scope  
        check if it exists in the program
        """
        if ID !=None: 
            ID = ID.getText()
            var_symbol = self.st.lookup(ID)
            if var_symbol !=None:    
                pass
            else: 
                print("ERROR:", "varible referanced but never assinged "+" '"+ID+"' "+"on line", line_number) 
        
        if ID !=None: 
            ID = ID
            var_symbol = self.st.lookup(ID)
            if var_symbol !=None:    
                pass
            else: 
                print("ERROR:", "varible referanced but never assinged"+" '" + ID + "' "+"on line", line_number)
        else: 
            pass        
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by DecafParser#var_decal.
    def visitVar_decal(self, ctx:DecafParser.Var_decalContext):
        line_number = ctx.start.line
        var_name = ctx.var_name(0).id(0).getText()
        var_value = ctx.var_value()
        
        if self.st.lookup(var_name) !=None:
            if self.st.lookup(var_name).type == "array" and ctx.assign_op: 
                value = var_value.getText()
                """
                check if an array is being evaluated to anything but an array
                """
                try:
                    if self.st.lookup(value).type !="int": 
                        print("ERROR: cannot evaluate array to int, line number:", line_number)
                    else: 
                        int(value)
                except: 
                    print("ERROR: cannot evaluate array to int, line number:", line_number)
                
        """
        check if a varible is decalred twice
        """
        if "=" in ctx.getText(): 
            pass
        else: 
            
            if self.st.probe(var_name ) !=None: 
                    print("ERROR: varible", "'"+var_name +"'", "decalred twice"," on line", line_number)
            else: 
                for i in range (len(ctx.var_name())):
                        if "[" in var_name:
                            Feild_decalsysmbol = VarSymbol(
                                    id = var_name.id().getText(),
                                    type = "array",
                                    line = line_number,
                                    size = 8,
                                    mem = SymbolTable.HEAP
                                    )
                            self.st.addSymbol(Feild_decalsysmbol)
                        else:
                            if ctx.var_type(0) !=None:
                                Feild_decalsysmbol = VarSymbol(
                                        id =  ctx.var_name(i).id(0).getText(),
                                        type = ctx.var_type(0).getText(),
                                        line = line_number,
                                        size = 8,
                                        mem = SymbolTable.STACK
                                        )
                                self.st.addSymbol(Feild_decalsysmbol)
                                
        VarNames = ctx.var_name()
        for i in range(len(VarNames)):
            for j in range(i + 1, len(VarNames)):
                if VarNames[i].getText() == VarNames[j].getText(): 
                    print("ERROR: varible", "'"+VarNames[i].getText()+"'", "decalred twice"," on line", line_number)
                else:
                    for k in VarNames:
                        Feild_decalsysmbol = VarSymbol(
                                id = k,
                                type = type,
                                line = ctx.var_type(i),
                                size = 8,
                                mem = SymbolTable.STACK
                                )                
                        self.st.addSymbol(Feild_decalsysmbol)
        
        if ctx.assign_op() !=None:
            """var_name_type = self.st.lookup(var_name).type"""
            """
            check that the operands of "+="  and -= is not a boolean or int
            """
            if "+=" in ctx.assign_op().getText() or "-=" in ctx.assign_op().getText():    
                for items in ctx.var_name(): 
                    var_name =items.getText()
                    var_name_type = self.st.lookup(var_name).type
                    if var_name_type == "boolean": 
                        if ctx.var_value().getText() == "true" or ctx.var_value().getText() == "false": 
                            print("ERROR: cannot assign boolean here, line number:", line_number)
                        else: 
                            var_name_type = self.st.lookup(var_name).type
                            var_value_type = self.st.lookup(var_value.id().getText()).type
                            if var_name_type and var_value_type !="int":
                                print("ERROR: type int must be used when using", ctx.assign_op().getText(),"line number",line_number)
            else:
                if self.st.lookup(var_value.id()) !=None:
                    """
                    check a var_name is being assinged to the same type of var_value
                    """
                    if self.st.lookup(var_name).type != self.st.lookup(var_value.id().getText()).type:
                        var_name_type = self.st.lookup(var_name).type
                        var_value_type = self.st.lookup(var_value.id().getText()).type
                        print("cannot assign", var_name_type,"to", var_value_type)   
                else: 
                    if self.st.lookup(var_name) !=None:
                        if self.st.lookup(var_name).type == "int":
                            try:  
                                int(var_value.getText())
                            except:
                                pass
                                #var_name_type = self.st.lookup(var_name).type
                                #print("cannot assign", var_name_type,"to this type here", line_number )
                        
                        
                        
        if ctx.var_name(0).expr() !=None: 
            exprID = ctx.var_name(0).expr().getText()
            exprType = self.st.lookup(exprID).type
            """
            check the type of expression as it must be int
            """
            if exprType !="int":
                print("ERROR: expected int, got "+exprType+" instead, line number:", line_number)
        
        """
        check if an array has an int and not any other type
        """        
        if "[" in ctx.var_name(0).getText(): 
            if self.st.lookup(var_name).type != "array": 
                errorType = self.st.lookup(var_name).type
                print("ERROR: varible needs to be an array type not",errorType,"on line", line_number)    
        """
        check var name existed before it assinged
        """
        if var_name:
            var_symbol = self.st.lookup(var_name)
            if var_symbol !=None: 
                for i in range (len(ctx.var_name())):
                    if "=" in ctx.getText(): 
                        #get var_name from the text
                        var_name = ctx.var_name(i).id(0).getText()                              
                        #get symbol of vars from symbol table
                        var_symbol = self.st.lookup(var_name)
                        #get address of symbol
                        var_addr = var_symbol.getAddr()          
                        
                        self.body += 'movq ' + str(var_addr) + '(%rsp), %rax\n'
            else: 
               print("ERROR:", "varible referanced but never assinged "+"'"+var_name+"' "+"on line", line_number) 

                
        if var_value !=None:
            var_value = var_value.getText()
            if '()' in var_value:
                var_value = self.st.lookup(var_value)
                if var_symbol !=None: 
                    pass
                else: 
                    print("ERROR:", "varible referanced but never assinged "+"'"+var_name+"' "+"on line", line_number)
        return self.visitChildren(ctx)  
    # Visit a parse tree produced by DecafParser#var_name.
    def visitVar_name(self, ctx:DecafParser.Var_nameContext):
        int_litereal = ctx.int_litereal()
        line_number = ctx.start.line
        
        """
        check int lit is bigger than 0 as arrays are not alloud to have an array value of 0
        """
        if int_litereal !=None:
            int_litereal = int_litereal.getText()
            if int(int_litereal) > 0:
                pass
            else:
                print("ERROR: arrays of length zero are not allowed" +", line", line_number)  
        return self.visitChildren(ctx)
   
    #visit expression node in tree
    def visitExpr(self, ctx:DecafParser.ExprContext):
        line_number = ctx.start.line
        method_call = ctx.method_call()
        bin_oper = ""
    
        if ctx.expr(0) !=None:
            if ctx.expr(0).bin_op() !=None:
                bin_oper = ctx.expr(0).bin_op().getText()    
        if self.eq_op: 
            pass
        else:
            expressions = ctx.expr(0)
            if expressions !=None:
                if ctx.expr(0).location() and bin_oper !=None:
                    for items in ctx.expr():
                        locatons = items.getText()
                        """
                        check that the operands of bin_op are ints
                        """
                        if self.st.lookup(locatons).type !="int":
                             print("ERROR: can only use a airthmetic operation on ints", line_number)                         
                if ctx.expr(0) and bin_oper !=None:
                    if ctx.expr(0).location:
                        pass
                    else:
                        airth_op = ctx.expr(0).bin_op().airth_op().getText()    
                        if airth_op in expressions.getText():
                            operands = ctx.expr(0).getText().replace(airth_op, "")
                            listOfoperands = list(operands)
                            """
                            if operands are not loctions (meaning not varibles), try to chnage the 
                            type to int, if that fails throw error
                            """
                            for i in range(len(listOfoperands)):
                                try: 
                                    int(listOfoperands[i])
                                except: 
                                    print("ERROR: can only use a airthmetic operation on ints", line_number)
        """
        check if a method call in side of an expression is not void as it must be a type to 
        be evaluated to something for it to be used in an expression, void is anon type
        """
        method_expr_params = []    
        if method_call !=None:
            method_params = method_call.expr()
            if self.st.lookup(method_call.ID().getText()).type == "void":
                print("ERROR: for method to be used here, method must return something"+ " line numnber", line_number)
                if "()" in method_call.getText():
                    name = method_call.getText()
                    name = name.replace("()", "")
                    
                    for names in method_params:
                        method_expr_params = method_expr_params.append[names]    
                    if len(method_expr_params) < len(self.st.lookup(name).params):
                        print("ERROR: "+"method "+self.st.lookup(name).id+
                                 " epecting",len(self.st.lookup(name).params),"but got",len(method_expr_params),"on line",line_number)
                        
        return self.visitChildren(ctx)   
        
source = 'testdata/codegen/00-empty'
filein = open(source + '.dcf', 'r')
lexer = DecafLexer(ant.InputStream(filein.read()))

#create a token stream from the lexer
stream = ant.CommonTokenStream(lexer)

#create a new parser with the token stream as input
parser = DecafParser(stream)
tree = parser.program()

#create a new calc visitor
codegen_visitor = DecafCodeGenVisitor()
codegen_visitor.visit(tree)

#output code
code = codegen_visitor.head + codegen_visitor.body
print(code)

#save the assembly file
fileout = open(source + '.s', 'w')
fileout.write(code)
fileout.close()

#assemble and link, then execute code
os.system('gcc -static '+ source +'.s')