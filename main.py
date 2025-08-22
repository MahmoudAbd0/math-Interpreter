from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
while True:
    command = input('calc > ')
    lexer = Lexer(command)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    result = interpreter.visit(ast)

    print(result)