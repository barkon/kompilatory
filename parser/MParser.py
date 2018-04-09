import ply.yacc as yacc
import scanner
import data


def prod_str(p):
    str = ""
    for i in range(len(p)):
        str += "| {0} ".format(p[i])
    return str


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
        """if_else_instr : IF '(' condition ')' instruction %prec IFX
                        | IF '(' condition ')' instruction ELSE instruction"""
        else_inst = p[7] if len(p) == 8 else None
        p[0] = data.IfElseInstr(p[3], p[5], else_inst)

    def p_while_inst(self, p):
        """while_instr : WHILE '(' condition ')' instruction"""
        p[0] = data.WhileInstr(p[3], p[5])

    def p_for_inst(self, p):
        """for_instr : FOR for_init instruction"""
        p[0] = data.ForInstr(p[2], p[3])

    def p_for_init(self, p):
        """for_init : ID '=' for_init_var ':' for_init_var"""
        p[0] = data.ForInit(p[1], p[3], p[5])

    def p_for_init_var(self, p):
        """for_init_var : number
                        | var_id"""
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
        """print_instr : PRINT print_vars ';'"""
        p[0] = data.PrintInstr(p[2])

    def p_print_vars(self, p):
        """print_vars : print_vars ',' print_var
                      | print_var"""
        if len(p) == 4:
            p[0] = data.PrintVarsList() if p[1] is None else p[1]
            p[0].add_var(p[3])
        else:
            p[0] = data.PrintVarsList()
            p[0].add_var(p[1])

    def p_print_var(self, p):
        """print_var : const
                     | var_id"""
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

    def p_num_id(self, p):
        """num_id : ID '[' INT ']'
                  | ID '[' INT ',' INT ']'"""
        p[0] = data.VarId(p[1], p[3]) if len(p) == 5 else data.VarId(p[1], p[3], p[5])

    def p_var_id(self, p):
        """var_id : ID
                  | num_id"""
        if len(p) == 2:
            p[0] = data.VarId(p[1])

    def p_assignment(self, p):
        """assignment : ID '=' expression
                      | ID '[' INT ']' '=' num_exp
                      | ID '[' INT ']' '=' var_id
                      | ID '[' INT ',' INT ']' '=' num_exp
                      | ID '[' INT ',' INT ']' '=' var_id
                      | op_assignment"""
        p[0] = data.AssignmentInstr(p[1], p[3]) if len(p) == 4 else p[1]

    def p_expression(self, p):
        """expression : ID
                      | num_exp
                      | matrix_expr"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = data.UnOperation(p[1], p[2]) if len(p) == 3 else p[2]

    def p_num_exp(self, p):
        """num_exp : number
                   | number_op
                   | '-' num_exp
                   | '(' num_exp ')'"""
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = data.NumberUnOp(p[1], p[2])
        elif len(p) == 4:
            p[0] = p[2]
        elif len(p) == 5:
            p[0] = data.VarId(p[1], p[3])
        else:
            p[0] = data.VarId(p[1], p[3], p[5])

    def p_matrix_expr(self, p):
        """matrix_expr : matrix_init
                       | matrix_op
                       | '-' matrix_expr
                       | '(' matrix_expr ')'"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = data.MatrixUnOp(p[1], p[2]) if len(p) == 3 else p[2]

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

    def p_matrix_op(self, p):
        """matrix_op : matrix_expr dot_op matrix_expr
                     | ID dot_op matrix_expr
                     | matrix_expr dot_op ID
                     | ID dot_op ID
                     | matrix_expr '\\''
                     | ID '\\''"""
        # print('matrix op:', p)
        p[0] = data.MatrixBinOp(p[2], p[1], p[3]) if len(p) == 4 else data.MatrixUnOp(p[2], p[1])

    def p_dot_op(self, p):
        """dot_op : DOTPLUS
                  | DOTMINUS
                  | DOTMUL
                  | DOTDIV"""
        p[0] = p[1]

    def p_num_op(self, p):
        """num_op : '+'
                  | '-'
                  | '*'
                  | '/'"""
        p[0] = p[1]

    def p_number_op(self, p):
        """number_op : num_exp num_op num_exp
                     | var_id num_op num_exp
                     | num_exp num_op var_id
                     | var_id num_op var_id
                     | '-' var_id"""
        p[0] = data.NumberBinOp(p[2], p[1], p[3]) if len(p) == 4 else data.NumberUnOp(p[1], p[2])

    def p_as_op(self, p):
        """as_op : PLUSASSIGN
                 | MINUSASSIGN
                 | MULASSIGN
                 | DIVASSIGN"""
        p[0] = p[1]

    def p_op_assignment(self, p):
        """op_assignment : var_id as_op num_exp
                         | var_id as_op var_id"""
        p[0] = data.OpAssignmentInstr(p[1], p[2], p[3])

    def p_rel_op(self, p):
        """rel_op : '<'
                  | '>'
                  | EQ
                  | NEQ
                  | LESSEQ
                  | MOREEQ"""
        p[0] = p[1]

    def p_condition(self, p):
        """condition : num_exp rel_op num_exp
                     | var_id rel_op var_id
                     | var_id rel_op num_exp
                     | num_exp rel_op var_id"""
        p[0] = data.Condition(p[1], p[2], p[3])

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

