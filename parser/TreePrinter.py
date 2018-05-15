import AST

INDENT_TOKEN = '| '


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Const)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + str(self.value) + "\n"

    @addToClass(AST.LValue)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + self.name + \
               ("" if self.indexes is None else "[" + str(self.indexes[0]) +
                ("]" if len(self.indexes) == 1 is None else ", " + str(self.indexes[1]) + "]"))

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        return self.instructions.printTree(indent)

    @addToClass(AST.InstructionList)
    def printTree(self, indent=0):
        ret = ""
        for i in range(len(self.instr_list)):
            ret += self.instr_list[i].printTree(indent)
        return ret

    @addToClass(AST.AssignmentInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + str(self.op) + '\n' + INDENT_TOKEN * (indent+1) + str(self.name) + '\n' +\
               self.expr.printTree(indent+1)

    @addToClass(AST.IfElseInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + "IF\n" + self.cond.printTree(indent + 1) + self.instr.printTree(indent + 1) + \
            ("" if self.else_instr is None else INDENT_TOKEN * indent + "ELSE\n" +
                self.else_instr.printTree(indent + 1))

    @addToClass(AST.WhileInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + "WHILE\n" + self.cond.printTree(indent + 1) + self.instr.printTree(indent)

    @addToClass(AST.ForInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + "FOR\n" + self.for_assignment.printTree(indent + 1) + self.instr.printTree(indent)

    @addToClass(AST.ForInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + self.var + '\n' + self.fr.printTree(indent) + self.to.printTree(indent)

    @addToClass(AST.BreakInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'BREAK\n'

    @addToClass(AST.ContinueInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'CONTINUE\n'

    @addToClass(AST.ReturnInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'RETURN\n' + self.ret.printTree(indent+1)

    @addToClass(AST.PrintInstr)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'PRINT\n' + self.to_print.printTree(indent+1)

    @addToClass(AST.InstrBlock)
    def printTree(self, indent=0):
        return "" if self.instructions is None else self.instructions.printTree(indent+1)

    @addToClass(AST.EyeInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'EYE\n' + INDENT_TOKEN * (indent+1) + str(self.size) + '\n'

    @addToClass(AST.OnesInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'ONES\n' + INDENT_TOKEN * (indent+1) + str(self.size) + '\n'

    @addToClass(AST.ZerosInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'ZEROS\n' + INDENT_TOKEN * (indent+1) + str(self.size) + '\n'

    @addToClass(AST.BinOperation)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + str(self.op) + '\n' + self.larg.printTree(indent+1) \
               + self.rarg.printTree(indent+1)

    @addToClass(AST.UnOperation)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + str(self.op) + '\n' + self.arg.printTree(indent+1)

    @addToClass(AST.PrintVarsList)
    def printTree(self, indent=0):
        ret = ''
        for i in range(len(self.print_list)):
            ret += self.print_list[i].printTree(indent)
        return ret

    @addToClass(AST.MatrixRows)
    def printTree(self, indent=0):
        ret = INDENT_TOKEN * indent + '[\n'
        for i in range(len(self.rows)):
            ret += self.rows[i].printTree(indent+1)
        ret += INDENT_TOKEN * indent + ']\n'
        return ret

    @addToClass(AST.MatrixRow)
    def printTree(self, indent=0):
        ret = INDENT_TOKEN * indent + '[\n'
        for i in range(len(self.row)):
            ret += INDENT_TOKEN * (indent+1) + str(self.row[i])
        ret += INDENT_TOKEN * indent + ']\n'
        return ret
