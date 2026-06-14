from mylang.tokenizer.tokenizer import Tokenizer
from mylang.parser.parser import Parser
from mylang.compiler.compiler import Compiler
from mylang.interpreter.interpreter import Interpreter

def main():

    print("0 for default, 1 for user input\n")
    choice = input()

    if choice == "0":
        code = "3 - 5"
    elif choice == "1":
        print("format can only be binary operation of + or - between two integers\n")
        code = input()
    else:
        raise RuntimeError(f"invalid input")

    #RUN TOKENIZER
    #tokenizer = list(Tokenizer(code))
    #print(tokenizer)

    #RUN PARSER
    #parser = Parser(list(Tokenizer(code)))
    #print(parser.parse())

    #RUN COMPILER
    #compiler = Compiler(Parser(list(Tokenizer(code))).parse())
    #for bytecode in compiler.compile():
    #    print(bytecode)

    #RUN INTERPRETER
    Interpreter(list(Compiler(Parser(list(Tokenizer(code))).parse()).compile())).interpret()

    #RUN INTERPRETER V2
    #tokens = list(Tokenizer(code))
    #tree = Parser(tokens).parse()
    #bytecode = list(Compiler(tree).compile())
    #Interpreter(bytecode).interpret()






if __name__ == "__main__":
    main()