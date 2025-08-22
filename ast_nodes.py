from dataclasses import dataclass
from typing import Any

@dataclass
class NumberNode:
    value: int
    def __repr__(self):
        return str(self.value)


@dataclass
class BinOpNode:
    left: Any
    op: Any
    right: Any
    
    def __repr__(self) :
        return f"({self.left} {self.op.type.name} {self.right})"
    
