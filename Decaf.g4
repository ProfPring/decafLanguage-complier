grammar Decaf;

/*
  LEXER RULES
  -----------
  Lexer rules define the basic syntax of individual words and symbols of a
  valid Decaf program. Lexer rules follow regular expression syntax.
*/
/*
key words and symbols
 */
CLASS : 'class';
PROGRAM: 'Program';
LCURLY : '{';
RCURLY : '}';
LSQURE: '[';
RSQURE: ']';
LROUND: '(';
RROUND: ')';
IF: 'if';
FOR: 'for';
VOID: 'void';
SEMICOLON: ';';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
CALLOUT: 'callout';
TRUE: 'true';
FALSE: 'false';
PLUS: '+';
COMMA: ',';
BOOLEAN: 'boolean';
INT: 'int';
EXCAL: '!';
EQ: '=';
MINUS: '-';
ELSE: 'else';
 LOGICAL_NOT: '!=';
DOUBLE_EQ: '==';
TIMES: '*';  
FORWARD_SLASH: '/' ;
PERCENT: '%';
LOGICAL_AND: '&&';
LOGICAL_OR:'||';
LESS_THAN: '<';
MORE_THAN: '>' ;
LESS_THAN_EQ: '<=';
MORE_THAN_EQ: '>=';
PLUS_EQ: '+=';
MINUS_EQ: '-=';
/*
key of words and symbols
 */

// APLHA rule is all the letters in the alphabet and a undersocre
fragment APLHA: [a-zA-Z_];
// aplha numeric rule, this rule allows any letter of the aplhabet or a digit
fragment APLHA_NUM: APLHA | DIGIT;

// an ID can be any letter from the aplha rule and zero or more numbers
ID: APLHA APLHA_NUM*;
//digit rule can be any number between 0 and 9 but not double digit numbers such as 10
fragment DIGIT: [0-9]; 
//decimels can be any number 
DECIMEL_LITEREAL: DIGIT+;
//hex digits can be a digit or any letter between a and f upercase and lowercase
fragment HEX_DIGIT: (DIGIT | [a-fA-F]);
//hex lit must start with an 0x and can be any 1 or more hex digits  
HEX_LITEREAL: '0x' HEX_DIGIT+ ;

//type is either int or boolean
fragment TYPE:(INT| BOOLEAN);
//char rule shows was is not alloud in the char 
fragment CHAR: ~('\'' | '"' | '\\') | '\\' [nt'"\\];
//char lit must be souranded by singluar qoutes
CHAR_LITERAL:  '\''CHAR?'\'';
// stirng lit allows zero or more chars sournded by double qoutes
STRING_LITERAL: '"'CHAR*'"';
//skip all white space
WS : [ \t\r\n\f]+ -> skip;
// skip all things after "//" charectors
LINE_COMMENT: '//' ~[\r\n]* -> skip;

/* 
  PARSER RULES
  ------------
  Parser rules are all lower case, and make use of lexer rules defined above
  and other parser rules defined below. Parser rules also follow regular
  expression syntax.

  parser rules are used to outline the syntax of the decaf langugae. 


   a pipe ("|") means or and therefor if a rule contrains the or symbol it means it can be either or but not both
   for example the expression a | b means a or b


   when parentheses are used this is used to group rules together for example "(A | B)" a and b are grouped almpst making one rule in its self

   lexer rules must be used in parser as if they are it would break the decad_parser.py and creates rules that are not accounted for, thus creating bugs that cannot be fixed
*/

/*
a program is donated by word class and program and then "{" 
a field declartion can follow and a meothd declaration can also follow in any order
*/
program: CLASS PROGRAM LCURLY feild_decal* method_decl* RCURLY;

int_litereal: DECIMEL_LITEREAL 
            | HEX_LITEREAL;

bool_literal: TRUE | FALSE;

assign_op: EQ 
        | MINUS_EQ 
        | PLUS_EQ;

literal: int_litereal
        | STRING_LITERAL
        | CHAR_LITERAL 
        | bool_literal;

airth_op: PLUS 
        | MINUS 
        | TIMES 
        | FORWARD_SLASH 
        | PERCENT;

rel_op: LESS_THAN 
      | MORE_THAN 
      | LESS_THAN_EQ 
      | MORE_THAN_EQ;

eq_op: DOUBLE_EQ |LOGICAL_NOT;

cond_op:LOGICAL_AND 
      | LOGICAL_OR;

/*
for readability the id rule has been deffined as a parser rule. 
for ease of use the method_name has been defined as the id parser rule as this
allows ease of access in the semantic code the check for errors in the written decaf language 
 */
id: ID;
method_name: id;

/*
in the same vien of thinking the field decal rule has  been split into many 
smaller rules as this allows readability of the semantic code and ease of access

it should be noted the field decal has been tested on the parser tests like the rest of the followng rules
 */

feild_name: id| id LSQURE int_litereal RSQURE;
field_type: (INT| BOOLEAN);
feild_decal:  feild_name SEMICOLON 
          |field_type (COMMA? feild_name)* SEMICOLON
          | field_type feild_name SEMICOLON
          | (COMMA? feild_name)* SEMICOLON;

/*
a loction rule is used after a varible has been decleared 
as to say "this the loction of the ID.
 */
location: (id) | (id) RSQURE expr LSQURE; 

bin_op: airth_op 
      | rel_op
      | eq_op
      | cond_op
      | assign_op;

//this essentially the print rule 
callout_arg: (expr | STRING_LITERAL);

expr: location
      | rel_op
      | method_call 
      | literal
      | expr bin_op expr
      | MINUS expr
      | LROUND expr RROUND; 

//meothd call is used when a method has already been made and is being called upon to be executed
method_call: id LROUND ( COMMA? expr )* RROUND
            | CALLOUT LROUND STRING_LITERAL (COMMA? callout_arg)* RROUND;

//a var name can just be an ID or an array for example a[id] or a[b] 
var_name: (id) | (id)* LSQURE (int_litereal | expr ) RSQURE;
var_type:(INT| BOOLEAN);
//the var value is what a varuble can be assinged too 
var_value: (expr* id | var_name |expr* location | expr* DECIMEL_LITEREAL | expr* DIGIT |expr* method_call | literal); 

/*
a var var_decal can be given by giving a type, and and a name along, or can be given by 
a name and then a value. the var_decal always ends with a semi colon
*/
var_decal: (var_type)* (COMMA? var_name )* SEMICOLON
         |  var_name assign_op var_value SEMICOLON
         |  var_name assign_op var_name SEMICOLON;
//method params can be an type followed an id or just a an id. this is checked semanticly in the semantic checking code
method_params: ((INT | BOOLEAN) id);
method_type: (INT | BOOLEAN | VOID);
method_param_type: (INT | BOOLEAN);
method_Param_names: (APLHA | id);
//method decal must be a type, and id, followed bu a "(" and then a method param type, and param name followed by a ")" and then a block
method_decl: method_type (id)* LROUND (COMMA? method_param_type method_Param_names)* RROUND block;

//break con is used for ease of use and readability in the semantic code
breaknCon: BREAK SEMICOLON | CONTINUE SEMICOLON;
//statment rule includes if, for, return, a meothd call, and so on
/*
an if statment should look as such "if(expr)block"
a for loop must be as such "for id = expr, expr block
 */
statement: location assign_op expr SEMICOLON
          | method_call SEMICOLON
          | IF LROUND expr RROUND block (ELSE block)?  
          | FOR (id) EQ expr COMMA expr block
          | RETURN expr* SEMICOLON
          | breaknCon
          | block;
//block can contain any zero or more var_decals or statments
block: LCURLY var_decal* statement* RCURLY;
