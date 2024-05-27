import unittest
from lexer.lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        lexer = Lexer("int a = 5;")
        tokens = lexer.tokenize()
        expected_tokens = [
            ('ID', 'int'), ('ID', 'a'), ('OP', '='),
