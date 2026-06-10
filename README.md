# Python Interpreter

A Python interpreter (and compiler).

## Goals

This project follows the full execution pipeline of a programming language:

1. **Tokenizer** – converts source code into tokens. (DONE)
2. **Parser** – converts tokens into an Abstract Syntax Tree (AST). (DONE)
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
pytest -v
```

## Running Main

```bash
python3 -m mylang.main
```

## Project Structure (will be changed as project evolves)

```text
Python-Interpreter/
├── src/
│   └── mylang/
│       ├── tokenizer/
│       │   ├── token.py
│       │   ├── tokenizer.py
│       │   └── __init__.py
│       │
│       ├── parser/
│       │   ├── ast.py
│       │   ├── parser.py
│       │   └── __init__.py
│       │
│       └── main.py
│
├── tests/
│   ├── test_tokenizer.py
│   ├── test_parser.py
│
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore

```

## Author

Fun Python project to explore and play around with the concepts and algorithms that are needed to implement a programming language like Python