from lexer import Lexer
while True:
    command = input('calc > ')
    lexer = Lexer(command)
    tokens = lexer.generate_tokens()
    print(tokens)