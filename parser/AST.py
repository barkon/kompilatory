
class Node(object):
    def __str__(self):
        return self.printTree()


class Const(Node):
    def __init__(self, value, line):
        self.value = value
        self.line = line


class Integer(Const):
    pass


class Float(Const):
    pass


class String(Const):
    pass


class LValue(Node):
    def __init__(self, name, indexes, line):
        self.name = name
        self.indexes = indexes if indexes is not None else []
        self.line = line


class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class InstructionList(Node):
    def __init__(self):
        self.instr_list = []

    def add_instruction(self, instr):
        self.instr_list.append(instr)


class AssignmentInstr(Node):
    def __init__(self, name, op, expr, line):
        self.name = name
        self.op = op
        self.expr = expr
        self.line = line


class IfElseInstr(Node):
    def __init__(self, cond, instr, else_instr):
        self.cond = cond
        self.instr = instr
        self.else_instr = else_instr


class WhileInstr(Node):
    def __init__(self, cond, instr, line):
        self.cond = cond
        self.instr = instr
        self.line = line
        
        
class ForInstr(Node):
    def __init__(self, for_init, instr):
        self.for_init = for_init
        self.instr = instr


class ForInit(Node):
    def __init__(self, var, fr, to, line):
        self.var = var
        self.fr = fr
        self.to = to
        self.line = line


class BreakInstr(Node):
    def __init__(self, line):
        self.line = line


class ContinueInstr(Node):
    def __init__(self, line):
        self.line = line


class ReturnInstr(Node):
    def __init__(self, ret, line):
        self.ret = ret
        self.line = line


class PrintInstr(Node):
    def __init__(self, to_print, line):
        self.to_print = to_print
        self.line = line


class InstrBlock(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class EyeInit(Node):
    def __init__(self, size, line):
        self.size = size
        self.line = line


class OnesInit(Node):
    def __init__(self, size, line):
        self.size = size
        self.line = line


class ZerosInit(Node):
    def __init__(self, size, line):
        self.size = size
        self.line = line


class BinOperation(Node):
    def __init__(self, op, larg, rarg, line):
        self.op = op
        self.larg = larg
        self.rarg = rarg
        self.line = line


class UnOperation(Node):
    def __init__(self, op, arg, line):
        self.op = op
        self.arg = arg
        self.line = line


class PrintVarsList(Node):
    def __init__(self):
        self.print_list = []

    def add_var(self, var):
        self.print_list.append(var)


class MatrixRows(Node):
    def __init__(self, line):
        self.line = line
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)


class MatrixRow(Node):
    def __init__(self, line):
        self.line = line
        self.row = []

    def add_elem(self, elem):
        self.row.append(elem)

    def add_from_scope(self, elem1, step, elemn):
        tmp = elem1
        while tmp <= elemn:
            self.row.append(tmp)
            tmp += step
