from mylang.tokenizer.tokenizer import Tokenizer
from mylang.parser.parser import Parser

def main():
    code = "3 - 5"
    parser = Parser(list(Tokenizer(code)))
    print(parser.parse())

if __name__ == "__main__":
    main()