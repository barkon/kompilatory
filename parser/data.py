
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
        self.inst_list = []

    def add_instruction(self, instruction):
        self.inst_list.append(instruction)


class AssignmentInstr(object):
    def __init__(self, id, expr):
        self.id = id
        self.expr = expr


