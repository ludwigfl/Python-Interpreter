import pytest
from mylang.tokenizer import Token, Tokenizer, TokenType

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

def test_tokenizer_addition_and_subtraction_with_whitespace():
    tokens = list(Tokenizer("         3-              5                +               2"))
    assert tokens == [
        Token(TokenType.INT, 3),
        Token(TokenType.MINUS),
        Token(TokenType.INT, 5),
        Token(TokenType.PLUS),
        Token(TokenType.INT, 2),
        Token(TokenType.EOF),
    ]

def test_tokenizer_raise_error_on_garbage():
    with pytest.raises(RuntimeError):
        list(Tokenizer("$"))

@pytest.mark.parametrize(
    ["code", "token"],
    [
        ("+", Token(TokenType.PLUS)),
        ("-", Token(TokenType.MINUS)),
        ("3", Token(TokenType.INT, 3)),
    ],
)
def test_tokenizer_recognizes_each_token(code: str, token: Token):
    tokens = list(Tokenizer(code))
    assert tokens == [
        token,
        Token(TokenType.EOF)
    ]