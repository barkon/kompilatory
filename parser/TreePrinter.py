import data

INDENT_TOKEN = '| '

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

    @addToClass(data.BreakInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'BREAK\n'

    @addToClass(data.ContinueInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'CONTINUE\n'

    @addToClass(data.ReturnInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'RETURN\n' + self.ret.printTree(indent+1)

    @addToClass(data.PrintInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'PRINT\n' + self.to_print.printTree(indent+1)

    @addToClass(data.InstrBlock)
    def printTree(self, indent=0):
        return "" if self.instructions is None else self.instructions.printTree(indent+1)

    @addToClass(data.EyeInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'EYE\n' + self.size.printTree(indent+1)

    @addToClass(data.OnesInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'ONES\n' + self.size.printTree(indent+1)

    @addToClass(data.ZerosInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'ZEROS\n' + self.size.printTree(indent+1)

    @addToClass(data.BinOperation)
    def printTree(self, indent=0):
        return self.operator.printTree(indent) + self.larg.printTree(indent+1) + self.rarg.printTree(indent+1)

    @addToClass(data.UnOperation)
    def printTree(self, indent=0):
        return self.operator.printTree(indent) + self.arg.printTree(indent+1)

    @addToClass(data.PrintVarsList)
    def printTree(self, indent=0):
        ret = ''
        for i in range(len(self.print_list)):
            ret += self.print_list[i].printTree(indent)
        return ret

    @addToClass(data.MatrixRows)
    def printTree(self, indent=0):
        ret = INDENT_TOKEN * indent + '[\n'
        for i in range(len(self.rows)):
            ret += self.rows[i].printTree(indent+1)
        ret += INDENT_TOKEN * indent + ']\n'
        return ret

    @addToClass(data.MatrixRow)
    def printTree(self, indent=0):
        ret = INDENT_TOKEN * indent + '[\n'
        for i in range(len(self.row)):
            ret += self.row[i].printTree(indent+1)
        ret += INDENT_TOKEN * indent + ']\n'
        return ret
