from mylang.compiler import Bytecode, BytecodeType, Compiler
from mylang.parser import BinOp, Int

def test_compile_addition():
    tree = BinOp(
        "+",
        Int(3),
        Int(5)
    )
    bytecode = list(Compiler(tree).compile())
    assert bytecode == [
        Bytecode(BytecodeType.PUSH, 3),
        Bytecode(BytecodeType.PUSH, 5),
        Bytecode(BytecodeType.BINOP, "+"),
    ]

def test_compile_subtraction():
    tree = BinOp(
        "-",
        Int(3),
        Int(5)
    )
    bytecode = list(Compiler(tree).compile())
    assert bytecode == [
        Bytecode(BytecodeType.PUSH, 3),
        Bytecode(BytecodeType.PUSH, 5),
        Bytecode(BytecodeType.BINOP, "-"),
    ]