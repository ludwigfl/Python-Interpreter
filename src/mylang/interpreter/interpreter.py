from mylang.compiler.bytecode import Bytecode, BytecodeType
from .stack import Stack

class Interpreter:
    def __init__(self, bytecode: list[Bytecode]) -> None:
        self.stack = Stack()
        self.bytecode = bytecode
        self.ptr: int = 0

    def interpret(self) -> None:
        for byte in self.bytecode:
            if byte.type == BytecodeType.PUSH:
                self.stack.push(byte.value)

            elif byte.type == BytecodeType.BINOP:
                right = self.stack.pop()
                left = self.stack.pop()
                if byte.value == "+":
                    result = left + right
                elif byte.value == "-":
                    result = left - right
                else:
                    raise RuntimeError(f"Unknown operator{byte.value}")
                self.stack.push(result)
        
        print("operation completed")
        print(self.stack)