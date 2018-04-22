import ply.yacc as yacc
import scanner
import data

class MParser(object):

    def __init__(self):
        self.scanner = scanner

    tokens = scanner.tokens + scanner.literals

    precedence = (
       ('nonassoc', 'IFX'),
       ('nonassoc', 'ELSE'),
       ('left', ','),
       ('right', '=', 'PLUSASSIGN', 'MINUSASSIGN', 'MULASSIGN', 'DIVASSIGN'),
       ('left', 'EQ', 'NEQ'),
       ('left', '>', '<', 'LESSEQ', 'MOREEQ'),
       ('left', '+', '-'),
       ('left', '*', '/'),
       ('left', 'DOTPLUS', 'DOTMINUS'),#?
       ('left', 'DOTMUL', 'DOTDIV'),#?
       ('left', ':'),
    )

    def p_error(self, p):
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno,
                                                                                      scanner.find_tok_column(p),
                                                                                      p.type, p.value))
        else:
            print("Unexpected end of input")

    def p_program(self, p):
        """program : instructions_opt"""
        p[0] = data.Program(p[1])

    def p_instructions_opt_1(self, p):
        """instructions_opt : instructions """
        p[0] = data.InstructionsOpt(p[1])

    def p_instructions_opt_2(self, p):
        """instructions_opt : """

    def p_instructions(self, p):
        """instructions : instructions instruction
                        | instruction"""
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
                       | print_instr
                       | instr_block
                       | assignment ';'"""
        p[0] = p[1]

    def p_if_else_inst(self, p):
        """if_else_instr : IF '(' expression ')' instruction %prec IFX 
                         | IF '(' expression ')' instruction ELSE instruction
                         | IF '(' error ')' instruction  %prec IFX
                         | IF '(' error ')' instruction ELSE instruction """
        else_inst = p[7] if len(p) == 8 else None
        p[0] = data.IfElseInstr(p[3], p[5], else_inst)

    def p_while_inst(self, p):
        """while_instr : WHILE '(' expression ')' instruction
                       | WHILE '(' error ')' instruction """
        p[0] = data.WhileInstr(p[3], p[5])

    def p_for_inst(self, p):
        """for_instr : FOR for_init instruction"""
        p[0] = data.ForInstr(p[2], p[3])

    # def p_for_init(self, p):
    #     """for_init : ID '=' for_init_var ':' for_init_var"""
    #     p[0] = data.ForInit(p[1], p[3], p[5])

    def p_for_init(self, p):
        """for_init : ID '=' expression ':' expression"""
        p[0] = data.ForInit(p[1], p[3], p[5])

    def p_for_init_var(self, p):
        """for_init_var : number
                        | lvalue"""
        p[0] = p[1]

    def p_break_inst(self, p):
        """break_instr : BREAK ';'"""
        p[0] = data.BreakInstr()

    def p_continue_inst(self, p):
        """continue_instr : CONTINUE ';'"""
        p[0] = data.ContinueInstr()

    def p_return_instr(self, p):
        """return_instr : RETURN expression ';'"""
        p[0] = data.ReturnInstr(p[2])

    def p_print_instr(self, p):
        """print_instr : PRINT print_vars ';'
                       | PRINT error ';'"""
        p[0] = data.PrintInstr(p[2])

    # def p_print_vars(self, p):
    #     """print_vars : print_vars ',' print_var
    #                   | print_var"""
    #     if len(p) == 4:
    #         p[0] = data.PrintVarsList() if p[1] is None else p[1]
    #         p[0].add_var(p[3])
    #     else:
    #         p[0] = data.PrintVarsList()
    #         p[0].add_var(p[1])

    def p_print_vars(self, p):
        """print_vars : print_vars ',' expression
                      | expression"""
        if len(p) == 4:
            p[0] = data.PrintVarsList() if p[1] is None else p[1]
            p[0].add_var(p[3])
        else:
            p[0] = data.PrintVarsList()
            p[0].add_var(p[1])

    def p_print_var(self, p):
        """print_var : const
                     | lvalue"""
        p[0] = p[1]

    def p_complex_instr(self, p):
        """instr_block : '{' instructions '}'"""
        p[0] = data.InstrBlock(p[2])

    def p_number(self, p):
        """number : INT
                  | FLOAT"""
        p[0] = p[1]

    def p_const(self, p):
        """const : number
                 | STRING"""
        p[0] = data.Const(p[1])

    def p_lvalue(self, p):
        """lvalue : ID
                  | ID '[' INT ']'
                  | ID '[' INT ',' INT ']'"""
        if len(p) == 2:
            p[0] = data.LValue(p[1])
        else:
            p[0] = data.LValue(p[1], p[3]) if len(p) == 5 else data.LValue(p[1], p[3], p[5])

    def p_assignment(self, p):
        """assignment : lvalue assign_op expression"""
        p[0] = data.AssignmentInstr(p[1], p[2], p[3])

    def p_assign_op(self, p):
        """assign_op : '='
                     | PLUSASSIGN
                     | MINUSASSIGN
                     | MULASSIGN
                     | DIVASSIGN"""
        p[0] = p[1]

    def p_expression(self, p):
        """expression : number
                      | lvalue
                      | matrix_init
                      | '(' expression ')'
                      | '-' expression
                      | expression '\\''
                      | expression bin_op expression"""
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = data.UnOperation(p[1], p[2]) if p[1] == '-' else data.UnOperation(p[2], p[1])
        else:
            p[0] = p[2] if p[1] == '(' and p[2] == ')' else data.BinOperation(p[2], p[1], p[3])

    def p_bin_op(self, p):
        """bin_op : rel_op
                  | num_op
                  | dot_op"""
        p[0] = p[1]

    def p_rel_op(self, p):
        """rel_op : '<'
                  | '>'
                  | EQ
                  | NEQ
                  | LESSEQ
                  | MOREEQ"""
        p[0] = p[1]

    def p_num_op(self, p):
        """num_op : '+'
                  | '-'
                  | '*'
                  | '/'"""
        p[0] = p[1]

    def p_dot_op(self, p):
        """dot_op : DOTPLUS
                  | DOTMINUS
                  | DOTMUL
                  | DOTDIV"""
        p[0] = p[1]

    def p_matrix_init(self, p):
        """matrix_init : eye
                       | ones
                       | zeros
                       | '[' matrix_rows ']'
                       | '[' scopes ']'"""
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_eye(self, p):
        """eye : EYE '(' INT ')' """
        p[0] = data.EyeInit(p[3])

    def p_ones(self, p):
        """ones : ONES '(' INT ')' """
        p[0] = data.OnesInit(p[3])

    def p_zeros(self, p):
        """zeros : ZEROS '(' INT ')' """
        p[0] = data.ZerosInit(p[3])

    def p_matrix_rows(self, p):
        """matrix_rows : matrix_rows ';' row_elems
                       | row_elems """
        if len(p) == 4:
            p[0] = data.MatrixRows() if p[1] is None else p[1]
            p[0].add_row(p[3])
        else:
            p[0] = data.MatrixRows()
            p[0].add_row(p[1])

    def p_row_elems(self, p):
        """row_elems : row_elems ',' number
                     | number """
        if len(p) == 4:
            p[0] = data.MatrixRow() if p[1] is None else p[1]
            p[0].add_elem(p[3])
        else:
            p[0] = data.MatrixRow()
            p[0].add_elem(p[1])

    def p_scopes(self, p):
        """scopes : scope
                | scopes ';' scope """

        if len(p) == 4:
            p[0] = data.MatrixRows() if p[1] is None else p[1]
            p[0].add_row(p[3])
        else:
            p[0] = data.MatrixRows()
            p[0].add_row(p[1])

    def p_scope(self, p):
        """scope : INT ':' INT
                | number ':' number ':' number"""

        p[0] = data.MatrixRow()
        if len(p) == 4:
            p[0].add_from_scope(p[1], 1, p[3])
        else:
            p[0].add_from_scope(p[1], p[3], p[5])
