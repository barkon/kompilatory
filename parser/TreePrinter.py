import data

INDENT_TOKEN = "| "


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:


    @addToClass(data.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)


    @addToClass(data.Const)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + str(self.value) + "\n"

    @addToClass(data.LValue)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + self.name + \
                ("" if self.row_index is None else ("[" + self.row_index + \
                 "]" if self.column_index is None else ", " + self.column_index + "]"))

    @addToClass(data.Program)
    def printTree(self, indent=0):
        return self.instructions_opt.printTree(indent)

    @addToClass(data.InstructionsOpt)
    def printTree(self, indent=0):
        return "" if self.instructions is None else self.instructions.printTree(indent)

    @addToClass(data.InstructionList)
    def printTree(self, indent=0):
        ret = ""
        for i in range(len(self.instr_list)):
            ret += self.instr_list[i].printTree(indent)
        return ret

    @addToClass(data.AssignmentInstr)
    def printTree(self, indent=0):
        return self.name.printTree(indent) + self.op.printTree(indent + 1) + self.expr.printTree(indent + 1)

    @addToClass(data.IfElseInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + "IF\n" + self.cond.printTree(indent + 1) + self.instr.printTree(indent + 1) + \
            ("" if self.else_instr  is None else INDENT_TOKEN * indent + "ELSE\n" +
                self.else_instr.printTree(indent + 1))

    @addToClass(data.WhileInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + "WHILE\n" + self.cond.printTree(indent + 1) + self.instr.printTree(indent)

    @addToClass(data.ForInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + "FOR\n" + self.for_assignment.printTree(indent + 1) + self.instr.printTree(indent)

    @addToClass(data.ForInit)
    def printTree(self, indent=0):
        return self.var.printTree(indent) + self.fr.printTree(indent) + self.to.printTree(indent)