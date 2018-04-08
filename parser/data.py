
class Const(object):
    def __init__(self, value):
        self.value = value


class Integer(Const):
    pass


class Float(Const):
    pass


class VarId(object):
    def __init__(self, name, row_index=None, column_index=None):
        self.name = name
        self.row_index = row_index
        self.column_index = column_index


class Program(object):
    def __init__(self, instructions_opt):
        self.instructions_opt = instructions_opt


class InstructionsOpt(object):
    def __init__(self, instructions):
        self.instructions = instructions


class InstructionList(object):
    def __init__(self):
        self.instr_list = []

    def add_instruction(self, instr):
        self.instr_list.append(instr)


class AssignmentInstr(object):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class OpAssignmentInstr(object):
    def __init__(self, name, op, expr):
        self.name = name
        self.op = op
        self.expr = expr


class IfElseInstr(object):
    def __init__(self, cond, instr, else_instr):
        self.cond = cond
        self.instr = instr
        self.else_instr = else_instr


class WhileInstr(object):
    def __init__(self, cond, instr):
        self.cond = cond
        self.instr = instr
        
        
class ForInstr(object):
    def __init__(self, for_assignment, instr):
        self.for_assignment = for_assignment
        self.instr = instr


class ForInit(object):
    def __init__(self, var, fr, to):
        self.var = var
        self.fr = fr
        self.to = to


class BreakInstr(object):
    pass


class ContinueInstr(object):
    pass


class ReturnInstr(object):
    def __init__(self, ret):
        self.ret = ret


class PrintInstr(object):
    def __init__(self, to_print):
        self.to_print = to_print


class InstrBlock(object):
    def __init__(self, instructions):
        self.instructions = instructions


class EyeInit(object):
    def __init__(self, size):
        self.size = size


class OnesInit(object):
    def __init__(self, size):
        self.size = size


class ZerosInit(object):
    def __init__(self, size):
        self.size = size


class Operation(object):
    def __init__(self, operator, args):
        self.operator = operator
        self.args = args


class MatrixOp(Operation):
    def __init__(self, operator, args):
        super().__init__(operator, args)


class NumberOp(Operation):
    def __init__(self, operator, args):
        super().__init__(operator, args)


class Condition(object):
    def __init__(self, larg, op, rarg):
        self.larg = larg
        self.op = op
        self.rarg = rarg
