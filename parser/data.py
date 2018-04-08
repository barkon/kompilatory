
class Const(object):
    def __init__(self, value):
        self.value = value


class Integer(Const):
    pass


class Float(Const):
    pass


class Id(Const):
    pass


class Operation(object):
    def __init__(self, operator, args):
        self.operator = operator
        self.args = args


class InstructionList(object):
    def __init__(self):
        self.instr_list = []

    def add_instrruction(self, instr):
        self.instr_list.append(instr)


class AssignmentInstr(object):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class IfElseInstr(object):
    def __init__(self, cond, instr, else_instr):
        self.cond = cond
        self.instr = instr
        self.else_instr = else_instr


class WhileInstr(object):
    def __init__(self, cond, instr):
        self.conc = cond
        self.instr = instr
        
        
class ForInstr(object):
    def __init__(self, for_assignment, instr):
        self.for_assignment = for_assignment
        self.instr = instr
        

class BreakInstr(object):
    pass


class ContinueInstr(object):
    pass


class ReturnInstr(object):
    def __init__(self, ret):
        self.ret = ret


class ComplexInstr(object):
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


