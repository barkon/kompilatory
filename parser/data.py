
class Node(object):
    def __str__(self):
        return self.printTree()


class Const(Node):
    def __init__(self, value):
        self.value = value


class Integer(Const):
    pass


class Float(Const):
    pass


class String(Const):
    pass


class LValue(Node):
    def __init__(self, name, row_index=None, column_index=None):
        self.name = name
        self.row_index = row_index
        self.column_index = column_index


class Program(Node):
    def __init__(self, instructions_opt):
        self.instructions_opt = instructions_opt


class InstructionsOpt(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class InstructionList(Node):
    def __init__(self):
        self.instr_list = []

    def add_instruction(self, instr):
        self.instr_list.append(instr)


class AssignmentInstr(Node):
    def __init__(self, name, op, expr):
        self.name = name
        self.op = op
        self.expr = expr


class IfElseInstr(Node):
    def __init__(self, cond, instr, else_instr):
        self.cond = cond
        self.instr = instr
        self.else_instr = else_instr


class WhileInstr(Node):
    def __init__(self, cond, instr):
        self.cond = cond
        self.instr = instr
        
        
class ForInstr(Node):
    def __init__(self, for_assignment, instr):
        self.for_assignment = for_assignment
        self.instr = instr


class ForInit(Node):
    def __init__(self, var, fr, to):
        self.var = var
        self.fr = fr
        self.to = to


class BreakInstr(Node):
    pass


class ContinueInstr(Node):
    pass


class ReturnInstr(Node):
    def __init__(self, ret):
        self.ret = ret


class PrintInstr(Node):
    def __init__(self, to_print):
        self.to_print = to_print


class InstrBlock(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class EyeInit(Node):
    def __init__(self, size):
        self.size = size


class OnesInit(Node):
    def __init__(self, size):
        self.size = size


class ZerosInit(Node):
    def __init__(self, size):
        self.size = size


class BinOperation(Node):
    def __init__(self, operator, larg, rarg):
        self.operator = operator
        self.larg = larg
        self.rarg = rarg


class UnOperation(Node):
    def __init__(self, operator, arg):
        self.op = operator
        self.arg = arg


class PrintVarsList(Node):
    def __init__(self):
        self.print_list = []

    def add_var(self, var):
        self.print_list.append(var)


class MatrixRows(Node):
    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)


class MatrixRow(Node):
    def __init__(self):
        self.row = []

    def add_elem(self, elem):
        self.row.append(elem)

    def add_from_scope(self, elem1, step, elemn):
        tmp = elem1
        while tmp <= elemn:
            self.row.append(tmp)
            tmp += step
