from ast_nodes import NumberNode, BinOpNode
from tokens import TokenType

class Interpreter:
    def visit(self, node):
        if isinstance(node, NumberNode):
            return node.value
        
        elif isinstance(node, BinOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)

            if node.op.type == TokenType.PLUS:
                return left + right
            elif node.op.type == TokenType.MINUS:
                return left - right
            elif node.op.type == TokenType.MULTIPLY:
                return left * right
            elif node.op.type == TokenType.DIVISION:
                return left / right