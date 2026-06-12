from mylang.tokenizer.tokenizer import Tokenizer
from mylang.parser.parser import Parser
from mylang.compiler.compiler import Compiler

def main():
    code = "3 - 5"

    #RUN TOKENIZER
    #tokenizer = list(Tokenizer(code))
    #print(tokenizer)

    #RUN PARSER
    #parser = Parser(list(Tokenizer(code)))
    #print(parser.parse())

    #RUN COMPILER
    compiler = Compiler(Parser(list(Tokenizer(code))).parse())
    for bytecode in compiler.compile():
        print(bytecode)

if __name__ == "__main__":
    main()