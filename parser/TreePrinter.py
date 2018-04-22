import data

INDENT_TOKEN = '| '


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


class TreePrinter:

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
        return INDENT_TOKEN * indent + 'EYE\n' + INDENT_TOKEN * (indent+1) + str(self.size) + '\n'

    @addToClass(data.OnesInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'ONES\n' + INDENT_TOKEN * (indent+1) + str(self.size) + '\n'

    @addToClass(data.ZerosInit)
    def printTree(self, indent=0):
        return INDENT_TOKEN * indent + 'ZEROS\n' + INDENT_TOKEN * (indent+1) + str(self.size) + '\n'

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
            ret += str(self.row[i]) + '\n'
        ret += INDENT_TOKEN * indent + ']\n'
        return ret
