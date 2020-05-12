import antlr4 as ant
from DecafLexer import DecafLexer

filein = open('testdata/lexer/string3', 'r')
lexer = DecafLexer(ant.InputStream(filein.read()))


token = lexer.nextToken()
while(token.type != -1):
    print(lexer.symbolicNames[token.type])
    token = lexer.nextToken()