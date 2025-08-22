from lexer import Lexer
from parser import Parser
while True:
    command = input('calc > ')
    lexer = Lexer(command)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()

    print(tree)