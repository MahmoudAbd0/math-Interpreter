from tokens import TokenType, Token

DIGITS = '0123456789'
SPACES = ' \n\t'

class Lexer:
    def __init__(self, command):
        self.command = iter(command)
        self.current_char = None
        self.advance()

    def advance(self):
        """Move to the next character in the input"""
        try:
            self.current_char = next(self.command)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in SPACES:
                self.advance()

            elif self.current_char in DIGITS:
                tokens.append(self.generate_number())

            elif self.current_char == "+":
                tokens.append(Token(TokenType.PLUS))
                self.advance()

            elif self.current_char == "-":
                tokens.append(Token(TokenType.MINUS))
                self.advance()

            elif self.current_char == "*":
                tokens.append(Token(TokenType.MULTIPLY))
                self.advance()

            elif self.current_char == "/":
                tokens.append(Token(TokenType.DIVISION))
                self.advance()

            elif self.current_char == "(":
                tokens.append(Token(TokenType.LPAREN))
                self.advance()

            elif self.current_char == ")":
                tokens.append(Token(TokenType.RPAREN))
                self.advance()

            else:
                raise Exception(f"Illegal character: {self.current_char}")

        return tokens

    def generate_number(self):
        """Handle multi-digit numbers"""
        num_str = self.current_char
        self.advance()

        while self.current_char is not None and self.current_char in DIGITS:
            num_str += self.current_char
            self.advance()

        return Token(TokenType.NUMBER, int(num_str))
