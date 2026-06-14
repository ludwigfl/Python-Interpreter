from mylang.tokenizer.token_model import Token, TokenType
from .ast import BinOp, Int

class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.next_token_index: int = 0
    
    def eat(self, expected_token_type: TokenType) -> Token:
        next_token = self.tokens[self.next_token_index]
        self.next_token_index += 1
        if next_token.type != expected_token_type:
            raise RuntimeError(f"Expected {expected_token_type} but got {next_token!r}")
        return next_token
    
    def peek(self, skip: int = 0) -> TokenType | None:
        peek_at = self.next_token_index + skip

        if peek_at < len(self.tokens):
             return self.tokens[peek_at].type
        else:
            return None
        
    def parse(self) -> BinOp:
        left_op = self.eat(TokenType.INT)

        if self.peek() == TokenType.PLUS:
            op = "+"
            self.eat(TokenType.PLUS)
        else:
            op = "-"
            self.eat(TokenType.MINUS)
        
        right_op = self.eat(TokenType.INT)

        self.eat(TokenType.EOF)

        return BinOp(op, Int(left_op.value), Int(right_op.value))
