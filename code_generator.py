class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []

    def generate(self):
        for node in self.ast:
            if node[0] == 'assign':
                self.generate_assignment(node)
        return '\n'.join(self.code)

    def generate_assignment(self, node):
        _, id_token, expr = node
        id_name = id_token[1]
        expr_code = self.generate_expression(expr)
        self.code.append(f'MOV {id_name}, {expr_code}')

    def generate_expression(self, expr):
        if expr[0] == 'NUMBER':
            return expr[1]
        elif expr[0] == 'ID':
            return expr[1]
        elif expr[0] == 'OP':
            op, left, right = expr
            left_code = self.generate_expression(left)
            right_code = self.generate_expression(right)
            if op[1] == '+':
                return f'ADD {left_code}, {right_code}'
            elif op[1] == '-':
                return f'SUB {left_code}, {right_code}'
            elif op[1] == '*':
                return f'MUL {left_code}, {right_code}'
            elif op[1] == '/':
                return f'DIV {left_code}, {right_code}'
        return None

if __name__ == "__main__":
    import sys
    from lexer.lexer import Lexer
    from parser.parser import Parser
    from semantic.semantic_analyzer import SemanticAnalyzer

    with open(sys.argv[1], 'r') as file:
        input_code = file.read()
    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    semantic_analyzer = SemanticAnalyzer(ast)
    semantic_analyzer.analyze()
    code_generator = CodeGenerator(ast)
    code = code_generator.generate()
    print(code)
