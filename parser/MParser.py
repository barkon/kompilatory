import ply.yacc as yacc
import scanner
import data


class MParser(object):

    def __init__(self):
        self.scanner = scanner

    tokens = scanner.tokens + scanner.literals
    print('tokens:', tokens)

    precedence = (
       ('nonassoc', 'IFX'),
       ('left', 'DOTPLUS', 'DOTMINUS'),
       ('left', 'DOTMUL', 'DOTDIV'),
       ("left", '+', '-'),
       ("left", '*', '/'),
    )

    def p_error(self, p):
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, 0, p.type, p.value))
        else:
            print("Unexpected end of input")

    def p_program(self, p):
        """program : instructions_opt"""
        #print('program:', p)

    def p_instructions_opt_1(self, p):
        """instructions_opt : instructions """
        #print('instructions_opt_1:', p)

    def p_instructions_opt_2(self, p):
        """instructions_opt : """
        #print('instructions_opt_2:', p)

    def p_instructions(self, p):
        """instructions : instructions instruction
                        | instruction"""
        #print('instructions:', p)
        if len(p) == 3:
            p[0] = data.InstructionList() if p[1] is None else p[1]
            p[0].add_instruction(p[1])
        else:
            p[0] = data.InstructionList()
            p[0].add_instruction(p[1])


    def p_instruction(self, p):
        """instruction : if_else_instr
                       | while_instr
                       | for_instr
                       | break_instr
                       | continue_instr
                       | return_instr
                       | complex_instr
                       | assignment"""
        p[0] = p[1]
        #print('instruction:', p)

    def p_if_else_inst(self, p):
        """if_else_instr : IF '(' condition ')' instruction %prec IFX
                        | IF '(' condition ')' instruction ELSE instruction"""
        else_inst = p[7] if len(p) == 8 else None
        #print('if/else instruction:', p)
        p[0] = data.IfElseInstr(p[3], p[5], else_inst)


    def p_while_inst(self, p):
        """while_instr : WHILE '(' condition ')' instruction"""
        p[0] = data.WhileInstr(p[3], p[5])
        #print('while instruction:', p)

    def p_for_inst(self, p):
        """for_instr : FOR for_init instruction"""
        #print('for instruction:', p)

    def p_for_init(self, p):
        """for_init : ID '=' INT ':' INT"""
        #print('for init:', p)

    def p_break_inst(self, p):
        """break_instr : BREAK ';'"""
        #print('break:', p)

    def p_continue_inst(self, p):
        """continue_instr : CONTINUE ';'"""
        #print('continue:', p)

    def p_return_instr(self, p):
        """return_instr : RETURN expression ';'"""
        #print('return:', p)

    def p_complex_instr(self, p):
        """complex_instr : '{' instructions '}'"""
        #print('complex:', p)
        p[0] = data.InstructionList

    def p_const(self, p):
        """const : INT
                  | FLOAT
                  | STRING"""
        p[0] = p[1]
        #print('const', p)

    def p_assignment(self, p):
        """assignment : ID '=' expression ';'"""
        #print('assignment:', p)
        p[0] = data.AssignmentInstr(p[1], p[3])


    def p_expression(self, p):
        """expression : ID
                      | const
                      | initialization
                      | '(' expression ')'"""
        #print('expression:', p)

    def p_initialization(self, p):
        """initialization : eye"""
        #print('initialization:', p)

    def p_condition(self, p):
        """condition : expression"""
        #print('condition:', p)

    def p_eye(self, p):
        """eye : EYE '(' INT ')'"""
        #print('eye:', p)


