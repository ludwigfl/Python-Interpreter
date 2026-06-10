from mylang.parser import Parser, BinOp, Int

from mylang.tokenizer.token_model import Token, TokenType

def test_parsing_addition():
    tokens = [
        Token(TokenType.INT, 3),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 5),
        Token(TokenType.EOF),
    ]

    tree = Parser(tokens).parse()
    assert tree == BinOp(
        "+",
        Int(3),
        Int(5),
    )

def test_parsing_subtraction():
    tokens = [
        Token(TokenType.INT, 3),
        Token(TokenType.MINUS),
        Token(TokenType.INT, 5),
        Token(TokenType.EOF),
    ]

    tree = Parser(tokens).parse()
    assert tree == BinOp(
        "-",
        Int(3),
        Int(5),
    )