import ply.lex as lex
import sys

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

tokens = ['DOTPLUS', 'DOTMINUS', 'DOTMUL', 'DOTDIV', 'PLUSASSIGN', 'MINUSASSIGN', 'MULASSIGN', 'DIVASSIGN', 'LESSEQ',
          'MOREEQ', 'NEQ', 'EQ', 'ID', 'INT', 'FLOAT', 'STRING']\
         + list(reserved.values())

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


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)
    pass


def t_FLOAT(t):
    r"""[0-9]+(e(\+|\-)?|\.)[0-9]+"""
    t.value = float(t.value)
    return t


def t_INT(t):
    r"""\d+"""
    t.value = int(t.value)
    return t 


def t_ID(t):
    r"""[a-zA-Z_]\w*"""
    t.type = reserved.get(t.value, 'ID')
    return t


def t_STRING(t):
    r"""\"[^\"]*\""""
    return t


def t_comment(t):
    r"""[#].*"""
    pass


def t_error(t):
    print("Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

t_ignore = ' \t'
literals = ['+', '-', '*', '/', '(', ')', '=', '<', '>', '[', ']', '{', '}', ':', '\'', ',', ';']
lexer = lex.lex()


def find_tok_column(tok):
    last_cr = lexer.lexdata.rfind('\n', 0, tok.lexpos)
    if last_cr < 0:
        last_cr = 0
    return tok.lexpos - last_cr


def scan():
    fh = open(sys.argv[1], "r") if len(sys.argv) > 1 else open("example.txt")
    lexer.input(fh.read())
    for token in lexer:
        print("line %d: %s(%s)" % (token.lineno, token.type, token.value))
