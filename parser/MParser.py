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
       ('left', 'DOTPLUS', 'DOTMINUS'),
       ('left', 'DOTMUL', 'DOTDIV'),
       ('left', '+', '-'),
       ('left', '*', '/'),
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
        #print('program:', p)
        p[0] = data.Program(p[1])

    def p_instructions_opt_1(self, p):
        """instructions_opt : instructions """
        #print('instructions_opt_1:', p)
        p[0] = data.InstructionsOpt(p[1])

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
                       | print_instr
                       | instr_block
                       | assignment ';'"""
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
        p[0] = data.ForInstr(p[2], p[3])

    def p_for_init(self, p):
        """for_init : ID '=' for_init_var ':' for_init_var"""
        #print('for init:', p)
        p[0] = data.ForInit(p[1], p[3], p[5])

    def p_for_init_var(self, p):
        """for_init_var : number
                        | var_id"""
        #print('for init var:', p)
        p[0] = p[1]

    def p_break_inst(self, p):
        """break_instr : BREAK ';'"""
        #print('break:', p)
        p[0] = data.BreakInstr()

    def p_continue_inst(self, p):
        """continue_instr : CONTINUE ';'"""
        #print('continue:', p)
        p[0] = data.ContinueInstr()

    def p_return_instr(self, p):
        """return_instr : RETURN expression ';'"""
        #print('return:', p)
        p[0] = data.ReturnInstr(p[2])

    def p_print_instr(self, p):
        """print_instr : PRINT print_vars ';'"""
        #print('print:', p)
        p[0] = data.PrintInstr(p[2])

    def p_complex_instr(self, p):
        """instr_block : '{' instructions '}'"""
        #print('complex:', p)
        p[0] = data.InstrBlock(p[2])

    def p_number(self, p):
        """number : INT
                  | FLOAT"""
        #print('number:', p)
        p[0] = p[1]

    def p_const(self, p):
        """const : number
                 | STRING"""
        #print('const:', p)
        p[0] = data.Const(p[1])

    def p_var_id(self, p):
        """var_id : ID
                  | ID '[' INT ']'
                  | ID '[' INT ',' INT ']'"""
        #print('var id:', p)
        if len(p) == 2:
            p[0] = data.VarId(p[1])
        else:
            p[0] = data.VarId(p[1], p[3]) if len(p) == 5 else data.VarId(p[1], p[3], p[5])

    def p_print_vars(self, p):
        """print_vars : print_vars ',' print_var
                      | print_var"""
        #print('print vars:', p)
        if len(p) == 4:
            p[0] = data.PrintVarsList() if p[1] is None else p[1]
            p[0].add_var(p[3])
        else:
            p[0] = data.PrintVarsList()
            p[0].add_var(p[1])

    def p_print_var(self, p):
        """print_var : const
                     | var_id"""
        #print('print var', p)
        p[0] = p[1]

    def p_assignment(self, p):
        """assignment : var_id '=' expression
                      | op_assignment"""
        #print('assignment:', p)
        p[0] = data.AssignmentInstr(p[1], p[3]) if len(p) == 4 else p[1]

    def p_expression(self, p):
        """expression : var_id
                      | const
                      | matrix_expr
                      | number_op
                      | '-' expression
                      | '(' expression ')'"""
        #print('expression:', p)
        p[0] = p[1]

    def p_matrix_expr(self, p):
        """matrix_expr : matrix_init
                       | matrix_op"""
        #print('matrix expr:', p)
        p[0] = p[1]

    def p_matrix_init(self, p):
        """matrix_init : eye
                       | ones
                       | zeros
                       | '[' matrix_rows ']'"""
        #print('matrix init:', p)
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_eye(self, p):
        """eye : EYE '(' INT ')' """
        #print('eye:', p)
        p[0] = data.EyeInit(p[3])

    def p_ones(self, p):
        """ones : ONES '(' INT ')' """
        #print('ones:', p)
        p[0] = data.OnesInit(p[3])

    def p_zeros(self, p):
        """zeros : ZEROS '(' INT ')' """
        #print('zeros:', p)
        p[0] = data.ZerosInit(p[3])

    def p_matrix_rows(self, p):
        """matrix_rows : matrix_rows ';' row_elems
                       | row_elems """
        #print('matrix rows:', p)
        if len(p) == 4:
            p[0] = data.MatrixRows() if p[1] is None else p[1]
            p[0].add_row(p[3])
        else:
            p[0] = data.MatrixRows()
            p[0].add_row(p[1])

    def p_row_elems(self, p):
        """row_elems : row_elems ',' number
                     | number """
        #print('rows elems:', p)
        if len(p) == 4:
            p[0] = data.MatrixRow() if p[1] is None else p[1]
            p[0].add_elem(p[3])
        else:
            p[0] = data.MatrixRow()
            p[0].add_elem(p[1])

    def p_matrix_op(self, p):
        """matrix_op : matrix_expr DOTPLUS matrix_expr
                     | matrix_expr DOTMINUS matrix_expr
                     | matrix_expr DOTMUL matrix_expr
                     | matrix_expr DOTDIV matrix_expr
                     | matrix_expr '\\''"""
        #print('matrix op:', p)
        p[0] = data.MatrixOp(p[2], [p[1], p[3]]) if len(p) == 4 else data.MatrixOp(p[2], p[1])

    def p_number_op(self, p):
        """number_op : expression '+' expression
                     | expression '-' expression
                     | expression '*' expression
                     | expression '/' expression"""
        #print('number op:', p)
        p[0] = data.MatrixOp(p[2], [p[1], p[3]])

    def p_op_assignment(self, p):
        """op_assignment : var_id PLUSASSIGN expression
                         | var_id MINUSASSIGN expression
                         | var_id MULASSIGN expression
                         | var_id DIVASSIGN expression"""
        #print('op assignment:', p)
        p[0] = data.OpAssignmentInstr(p[1], p[2], p[3])

    def p_condition(self, p):
        """condition : expression '<' expression
                     | expression '>' expression
                     | expression EQ expression
                     | expression LESSEQ expression
                     | expression MOREEQ expression
                     | expression NEQ expression"""
        #print('condition:', p)
        p[0] = data.Condition(p[1], p[2], p[3])

