from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any

class BytecodeType(StrEnum):
    BINOP = auto()
    PUSH = auto()

@dataclass
class Bytecode: 
    type: Bytecode
    value: Any = None
