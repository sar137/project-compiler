class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        statements = []
        while self.current < len(self.tokens):
            statements.append(self.statement())
        return statements

    def statement(self):
        token = self.tokens[self.current]
        if token[0] == 'ID':
            return self.assignment()
        # Additional parsing rules for other statements
        return None

    def assignment(self):
        id_token = self.tokens[self.current]
        self.current += 2  # skip ID and '='
        expr = self.expression()
        self.current += 1  # skip ';'
        return ('assign', id_token, expr)

    def expression(self):
        term = self.term()
        while self.current < len(self.tokens) and self.tokens[self.current][0] == 'OP':
            op = self.tokens[self.current]
            self.current += 1
            term = (op, term, self.term())
        return term

    def term(self):
        factor = self.factor()
        while self.current < len(self.tokens) and self.tokens[self.current][0] == 'OP':
            op = self.tokens[self.current]
            self.current += 1
            factor = (op, factor, self.factor())
        return factor

    def factor(self):
        token = self.tokens[self.current]
        if token[0] == 'NUMBER':
            self.current += 1
            return token
        elif token[0] == 'ID':
            self.current += 1
            return token
        elif token[0] == 'LPAREN':
            self.current += 1
            expr = self.expression()
            self.current += 1  # skip ')'
            return expr
        return None

if __name__ == "__main__":
    import sys
    from lexer.lexer import Lexer

    with open(sys.argv[1], 'r') as file:
        input_code = file.read()
    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
