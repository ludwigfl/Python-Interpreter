from mylang.parser.ast import BinOp
from mylang.compiler.bytecode import Bytecode, BytecodeType
from typing import Generator


class Compiler:
    def __init__(self, tree: BinOp) -> None:
        self.tree = tree
    
    def compile(self) -> Generator[Bytecode, None, None]:
        left = self.tree.left
        yield Bytecode(BytecodeType.PUSH, left.value)

        right = self.tree.right
        yield Bytecode(BytecodeType.PUSH, right.value)

        yield Bytecode(BytecodeType.BINOP, self.tree.op)