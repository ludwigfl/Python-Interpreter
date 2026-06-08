# Python Interpreter

A Python interpreter (and compiler).

## Goals

This project follows the full execution pipeline of a programming language:

1. **Tokenizer** – converts source code into tokens.
2. **Parser** – converts tokens into an Abstract Syntax Tree (AST). (NOT DONE)
3. **Compiler** – converts the AST into bytecode. (NOT DONE)
4. **Interpreter (VM)** – executes the bytecode. (NOT DONE)

## Example

Input:

```python
1 + 2 - 3
```

Tokens:

```text
INT(1) PLUS INT(2) MINUS INT(3) EOF
```

## Running Tests

```bash
pytest
```

## Project Structure (will be changed as project evolves)

```text
src/
└── tokenizer/
    ├── token_model.py
    ├── tokenizer.py
    └── __init__.py

tests/
```

## Author

Fun Python project to explore and play around with the concepts and algorithms that are needed to implement a programming language like Python