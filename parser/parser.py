import ply.yacc as yacc
import scanner
import data


class MParser(object):

    def __init__(self):
        self.scanner = scanner

    tokens = scanner.tokens

    precedence = (
       ("left", '+', '-'),
       ("left", '*', '/'),
    )

    def p_error(self, p):
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno,
                                                                                      scanner.find_tok_column(p),
                                                                                      p.type, p.value))
        else:
            print("Unexpected end of input")

    def p_program(self, p):
        """program : instructions"""

    def p_instructions(self, p):
        """instructions : instructions instruction
                        | instruction"""
        if len(p) == 3:
            p[0] = data.InstructionList() if p[1] is None else p[1]
            p[0].add_instruction(p[1])
        else:
            p[0] = data.InstructionList()
            p[0].add_instruction(p[1])

    def p_empty(self, p):
        """empty : """
        p[0] = None

    def p_instruction(self, p):
        """instruction : assignment
                       | if_else_inst
                       | while_inst
                       | for_inst
                       | break_inst
                       | continue_inst
                       | return_inst
                       | nested_inst
                       | empty"""
        p[0] = p[1]

    def p_assignment(self, p):
        """assignment : ID '=' expression ';'"""
        p[0] = data.AssignmentInstr(p[1], p[3])

    def p_if_else_inst(self, p):
        """if_else_inst : IF '(' condition ')' instruction %prec IFX
                        | IF '(' condition ')' instruction ELSE instruction"""
        p[0] = data.
