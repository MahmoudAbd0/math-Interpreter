from tokens import TokenType
from ast_nodes import BinOpNode, NumberNode

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = None
        self.advance()


    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token == None:
            return None
        node = self.expression()
        return node
        

    def expression(self):
        node = self.term()
        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            self.advance()
            right = self.term()
            node = BinOpNode(node, op, right)
        return node
        

    def term(self):
        node = self.factor()
        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVISION):
            op = self.current_token
            self.advance()
            right = self.factor()
            node = BinOpNode(node, op, right)
        return node
        

    
    def factor(self):
        token = self.current_token
        if token == None:
            raise Exception("Unexpected end of input")
        
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        if token.type == TokenType.LPAREN:
            self.advance()
            node = self.expression()
            if self.current_token is None or self.current_token.type != TokenType.RPAREN:
                raise Exception("Expected ')'")
            self.advance()
            return node

        raise Exception(f"Unexpected token: {token}")


    