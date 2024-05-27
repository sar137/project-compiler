from lexer.lexer import Lexer
from parser.parser import Parser
from semantic.semantic_analyzer import SemanticAnalyzer
from codegen.code_generator import CodeGenerator

def main():
    with open('examples/example1.c', 'r') as file:
        input_code = file.read()

    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    print("Tokens:", tokens)

    parser = Parser(tokens)
    ast = parser.parse()
    print("AST:", ast)

    semantic_analyzer = SemanticAnalyzer(ast)
    semantic_analyzer.analyze()
    print("Symbol Table:", semantic_analyzer.symbol_table)

    code_generator = CodeGenerator(ast)
    code = code_generator.generate()
    print("Generated Code:", code)

if __name__ == "__main__":
    main()
