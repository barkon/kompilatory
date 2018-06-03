import AST
from Memory import *
from Exceptions import *
import inspect
from visit import *
import TypeChecker


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
        pass

    @when(AST.PrintVarsList)
    def visit(self, node):
        pass

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
        pass

    @when(AST.UnOperation)
    def visit(self, node):
        pass

    @when(AST.Matrix)
    def visit(self, node):
        pass

    @when(AST.MatrixRow)
    def visit(self, node):
        pass
