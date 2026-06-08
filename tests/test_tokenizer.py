from ..tokenizer import Token, Tokenizer, TokenType

def test_tokenizer_addition():
    tokens = list(Tokenizer("3 + 5"))
    assert tokens == [
        Token(TokenType.INT, 3),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 5),
        Token(TokenType.EOF),
    ]

def test_tokenizer_subtraction():
    tokens = list(Tokenizer("3 - 5"))
    assert tokens == [
        Token(TokenType.INT, 3),
        Token(TokenType.MINUS),
        Token(TokenType.INT, 5),
        Token(TokenType.EOF),
    ] 

def test_tokenizer_addition_and_subtraction():
    tokens = list(Tokenizer("3 - 5 + 2"))
    assert tokens == [
        Token(TokenType.INT, 3),
        Token(TokenType.MINUS),
        Token(TokenType.INT, 5),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 2),
        Token(TokenType.EOF),
    ] 