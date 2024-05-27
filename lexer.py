import re

class Lexer:
    def __init__(self, input_code):
        self.tokens = []
        self.current = 0
        self.input_code = input_code

    def tokenize(self):
        token_specification = [
            ('NUMBER', r'\d+'),
            ('ID', r'[A-Za-z_]\w*'),
            ('OP', r'[+\-*/=]'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('SEMICOLON', r';'),
            ('WHITESPACE', r'\s+'),
            ('MISMATCH', r'.')
        ]
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        for mo in re.finditer(tok_regex, self.input_code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                value = int(value)
            elif kind == 'WHITESPACE':
                continue
            self.tokens.append((kind, value))
        return self.tokens

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], 'r') as file:
        input_code = file.read()
    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    print(tokens)
