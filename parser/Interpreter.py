import AST
from Memory import *
from Exceptions import *
import inspect
from visit import *
from Operations import *
import TypeChecker


bin_op_map = {'+': plus, '-': sub, '*': mul, '/': div, '.+': dot_plus, '.-': dot_sub, '.*': dot_mul, './': dot_div,
              '==': eq, '!=': neq, '<=': leq, '>=': geq, '<': less, '>': greater}
un_op_map = {'-': neg, '\'': trans}



class Interpreter:
    def __init__(self):
        self.mem_stack = MemoryStack(Memory('global'))

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Integer)
    def visit(self, node):
        return node.value

    @when(AST.Float)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.LValue)
    def visit(self, node):
        if len(node.indexes) == 2:
            return self.mem_stack.get(node.name)[node.indexes[0]][node.indexes[1]]
        elif len(node.indexes) == 1:
            return self.mem_stack.get(node.name)[node.indexes[0]]
        else:
            return self.mem_stack.get(node.name)

    @when(AST.Program)
    def visit(self, node):
        self.visit(node.instructions)

    @when(AST.InstructionList)
    def visit(self, node):
        for instruction in node.instr_list:
            self.visit(instruction)

    @when(AST.AssignmentInstr)
    def visit(self, node):
        expr_val = self.visit(node.expr)
        prev_lval = self.mem_stack.get(node.lvalue.name)
        if prev_lval is not None:
            if node.op[0]!='=':
                expr_val = bin_op_map[node.op[0]](self.visit(node.lvalue), self.visit(node.expr))
            if len(node.lvalue.indexes) == 2:
                lval = self.mem_stack.get(node.lvalue.name)
                lval[node.lvalue.indexes[0]][node.lvalue.indexes[1]] = expr_val
                self.mem_stack.set(node.lvalue.name, lval)
            elif len(node.lvalue.indexes) == 1:
                lval = self.mem_stack.get(node.lvalue.name)
                lval[node.lvalue.indexes[0]] = expr_val
                self.mem_stack.set(node.lvalue.name, lval)
            else:
                self.mem_stack.set(node.lvalue.name, expr_val)
        else:
            self.mem_stack.insert(node.lvalue.name, expr_val)

    @when(AST.IfElseInstr)
    def visit(self, node):
        cond_val = self.visit(node.cond)
        if cond_val:
            self.mem_stack.push(Memory("if"))
            self.visit(node.instr)
            self.mem_stack.pop()
        elif node.else_instr is not None:
            self.mem_stack.push(Memory("else"))
            self.visit(node.else_instr)
            self.mem_stack.pop()

    @when(AST.WhileInstr)
    def visit(self, node):
        self.mem_stack.push(Memory("while"))
        while self.visit(node.cond):
            try:
                self.visit(node.instr)
            except BreakException:
                # self.mem_stack.pop()
                break
            except ContinueException:
                continue
        self.mem_stack.pop()

    @when(AST.ForInstr)
    def visit(self, node):
        varname, fr, to = self.visit(node.for_init)
        self.mem_stack.push(Memory("for"))
        self.mem_stack.insert(varname, fr.value)
        for i in range(fr.value, to.value):
            self.mem_stack.set(varname, i)
            try:
                self.visit(node.instr)
            except BreakException:
                # self.mem_stack.pop()
                break
            except ContinueException:
                continue
        self.mem_stack.pop()

    @when(AST.ForInit)
    def visit(self, node):
        return node.var, node.fr, node.to
        pass

    @when(AST.BreakInstr)
    def visit(self, node):
        raise BreakException

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
        self.visit(node.instructions)

    @when(AST.EyeInit)
    def visit(self, node):
        matrix = AST.Matrix(node.line)
        for i in range(self.visit(node.size)):
            row = AST.MatrixRow(node.line)
            for j in range(self.visit(node.size)):
                row.add_elem(0) if i != j else row.add_elem(1)
            matrix.add_row(row)
        return matrix

    @when(AST.OnesInit)
    def visit(self, node):
        matrix = AST.Matrix(node.line)
        for i in range(self.visit(node.size)):
            row = AST.MatrixRow(node.line)
            for j in range(self.visit(node.size)):
                row.add_elem(1)
            matrix.add_row(row)
        return matrix

    @when(AST.ZerosInit)
    def visit(self, node):
        matrix = AST.Matrix(node.line)
        for i in range(self.visit(node.size)):
            row = AST.MatrixRow(node.line)
            for j in range(self.visit(node.size)):
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

    @when(AST.Matrix)
    def visit(self, node):
        return node

    @when(AST.MatrixRow)
    def visit(self, node):
        return node
