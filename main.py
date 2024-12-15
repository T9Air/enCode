from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_program(source_code):
    # Create lexer instance
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    return tokens
    
    # # Create parser instance
    # parser = Parser(tokens)
    # ast = parser.parse()
    
    # # Create interpreter instance
    # interpreter = Interpreter(ast)
    # result = interpreter.interpret()
    # return result

if __name__ == "__main__":
    source = "2 + 9"
    result = run_program(source)
    print(result)