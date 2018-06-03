import AST
from Memory import *
from Exceptions import *
import inspect
from visit import *
from Operations import *
import TypeChecker


bin_op_map = {'+': plus, '-': sub, '*': mul, '/': div, '.+': dot_plus, '.-': dot_sub, '.*': dot_mul, './': dot_div}
un_op_map = {'-': neg, '\'': trans}


class Interpreter:
    def __init__(self):
        self.mem_stack = MemoryStack(Memory('global'))

    @on('node')
    def visit(self, node):
        pass

    @when(AST.ContinueInstr)
    def visit(self, node):
        raise ContinueException

    @when(AST.ReturnInstr)
    def visit(self, node):
        raise ReturnValueException(node.ret)

    @when(AST.PrintInstr)
    def visit(self, node):
        self.visit(node.to_print)

    @when(AST.PrintVarsList)
    def visit(self, node):
        print_string = ''
        for var in node.print_list:
            print_string += str(self.visit(var)) + ' '
        print(print_string)

    @when(AST.InstrBlock)
    def visit(self, node):
        for instr in node.instructions:
            self.visit(instr)

    @when(AST.EyeInit)
    def visit(self, node):
        matrix = AST.Matrix(node.line)
        for i in range(node.size):
            row = AST.MatrixRow(node.line)
            for j in range(node.size):
                row.add_elem(0) if i != j else row.add_elem(1)
            matrix.add_row(row)
        return matrix

    @when(AST.OnesInit)
    def visit(self, node):
        matrix = AST.Matrix(node.line)
        for i in range(node.size):
            row = AST.MatrixRow(node.line)
            for j in range(node.size):
                row.add_elem(1)
            matrix.add_row(row)
        return matrix

    @when(AST.ZerosInit)
    def visit(self, node):
        matrix = AST.Matrix(node.line)
        for i in range(node.size):
            row = AST.MatrixRow(node.line)
            for j in range(node.size):
                row.add_elem(0)
            matrix.add_row(row)
        return matrix

    @when(AST.BinOperation)
    def visit(self, node):
        larg = self.visit(node.larg)
        rarg = self.visit(node.rarg)
        return bin_op_map[node.op](larg, rarg)

    @when(AST.UnOperation)
    def visit(self, node):
        return un_op_map[node.op](node.arg)

    @when(AST.Matrix)   # nie jestem pewien czy to jest potrzebne
    def visit(self, node):
        return node

    @when(AST.MatrixRow)    # tak samo tu
    def visit(self, node):
        return node
