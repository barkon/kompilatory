import ply.lex as lex


class Scanner(object):

    def find_tok_column(self, tok):
        last_cr = self.lexer.lexdata.rfind('\n', 0, tok.lexpos)
        if last_cr < 0:
            last_cr = 0
        return tok.lexpos - last_cr

    def build(self):
        self.lexer = lex.lex(object=self)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        return self.lexer.token()

    literals = ['+', '-', '*', '/', '(', ')', '=', '<', '>', '[', ']', '{', '}', ':', '\'', ',', ';']

    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'for': 'FOR',
        'while': 'WHILE',
        'break': 'BREAK',
        'continue': 'CONTINUE',
        'return': 'RETURN',
        'eye': 'EYE',
        'zeros': 'ZEROS',
        'ones': 'ONES',
        'print': 'PRINT'
    }

    tokens = ['DOTPLUS', 'DOTMINUS', 'DOTMUL', 'DOTDIV', 'PLUSASSIGN', 'MINUSASSIGN', 'MULASSIGN', 'DIVASSIGN',
              'LESSEQ',
              'MOREEQ', 'NEQ', 'EQ', 'ID', 'INT', 'FLOAT', 'STRING'] + list(reserved.values())

    t_DOTPLUS = r'.\+'
    t_DOTMINUS = r'.-'
    t_DOTMUL = r'.\*'
    t_DOTDIV = r'./'
    t_PLUSASSIGN = r'\+='
    t_MINUSASSIGN = r'-='
    t_MULASSIGN = r'\*='
    t_DIVASSIGN = r'/='
    t_LESSEQ = r'<='
    t_MOREEQ = r'>='
    t_NEQ = r'!='
    t_EQ = r'=='

    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)
        pass

    def t_FLOAT(self, t):
        r"""[0-9]+(e(\+|\-)?|\.)[0-9]+"""
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r"""\d+"""
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r"""[a-zA-Z_]\w*"""
        t.type = Scanner.reserved.get(t.value, 'ID')
        return t

    def t_STRING(self, t):
        r"""\"[^\"]*\""""
        return t

    def t_comment(self, t):
        r"""[#].*"""
        pass

    def t_error(self, t):
        print("Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno))
        t.lexer.skip(1)

    t_ignore = ' \t'


