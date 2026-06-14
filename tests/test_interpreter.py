import pytest

from mylang.compiler import Compiler
from mylang.parser import Parser
from mylang.tokenizer import Tokenizer
from mylang.interpreter.interpreter import Interpreter

@pytest.mark.parametrize(
    ["code", "result"],
    [
        ("3 + 5", 8),
        ("3 - 5", -2),
        ("6 + 1", 7),
    ],
)
def test_simple_arithmetic(code: str, result:int):
    tokens = list(Tokenizer(code))
    tree = Parser(tokens).parse()
    bytecode = list(Compiler(tree).compile())
    interpreter = Interpreter(bytecode)
    interpreter.interpret()
    assert interpreter.stack.pop() == result


