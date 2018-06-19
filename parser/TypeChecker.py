import AST
import SymbolTable

class Matrix():
    def __init__(self, scopes):
        self.scopes = scopes if scopes is not None else []

typemap = dict()
for op in ['+', '-', '/', '*']:
    typemap[(op, 'int', 'int')] = 'int'
    typemap[(op, 'float', 'float')] = 'float'
    typemap[(op, 'int', 'float')] = 'float'
    typemap[(op, 'float', 'int')] = 'float'

for op in ['>', '<', '==', '!=', '>=', '<=']:
    typemap[(op, 'int', 'int')] = 'int'
    typemap[(op, 'float', 'float')] = 'int'
    typemap[(op, 'int', 'float')] = 'int'
    typemap[(op, 'float', 'int')] = 'int'

for op in ['.+', '.-', './', '.*']:
    typemap[(op, Matrix.__name__, Matrix.__name__)] = Matrix.__name__


for op in ['+=', '-=', '*=', '/=']:
    typemap[(op, 'int', 'int')] = 'int'
    typemap[(op, 'float', 'float')] = 'float'
    typemap[(op, 'int', 'float')] = 'float'
    typemap[(op, 'float', 'int')] = 'float'

forinitmap = dict()
forinitmap[('int', 'int')]  = 'int'


'''class Matrix:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size'''


class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    # def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.symtable = SymbolTable.SymbolTable(None, 'root')

    def visit_Integer(self, node):
        return 'int'

    def visit_String(self, node):
        return 'string'

    def visit_Float(self, node):
        return 'float'

    def visit_Program(self, node):
        if node.instructions is not None:
            self.visit(node.instructions)

    def visit_InstructionList(self, node):
        for instr in node.instr_list:
            self.visit(instr)

    def visit_BinOperation(self, node):
        # alternative usage,
        # requires definition of accept method in class Node
        type1 = self.visit(node.larg)
        type2 = self.visit(node.rarg)
        op = node.op
        op_type = typemap[(op, type1, type2)]
        if op_type is None:
            print('Incompatible types in binary expression in line:')
        return op_type

    def visit_EyeInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type != 'int':
            print('Incorrect argument type in eye function in line:')
        return Matrix([node.size, node.size])

    def visit_OnesInit(self, node):
        arg_type = self.visit(node.size)
        print(arg_type)
        if arg_type != 'int':
            print('Incorrect argument type in ones function in line:')
        return Matrix([node.size, node.size])

    def visit_ZerosInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type != 'int':
            print('Incorrect argument type in zeros function in line:')
        return Matrix([node.size, node.size])

    def visit_ForInstr(self, node):
        self.visit(node.for_init)
        self.symtable = self.symtable.pushScope('for')
        self.visit(node.instr)
        self.symtable = self.symtable.popScope()

    def visit_ForInit(self, node):
        fr_type = self.visit(node.fr)
        to_type = self.visit(node.to)
        if fr_type != 'int' or to_type != 'int':
            print("Not a valid type for for init in line: ", node.line)
        self.symtable.put(node.var, fr_type)

    def visit_WhileInstr(self, node):
        c_type = self.visit(node.cond)
        if c_type != 'int':
            print('Incorrect condition type in while instruction in line ', node.line)
        self.symtable = self.symtable.pushScope('while')
        self.visit(node.instr)
        self.symtable = self.symtable.popScope()

    def visit_ContinueInstr(self, node):
        symt = self.symtable
        while symt is not None and symt.name != 'while' and symt.name != 'for':
            symt = symt.parent
        if symt is None:
            print('Continue instruction outside of the loop in line ', node.line)

    def visit_BreakInstr(self, node):
        symt = self.symtable
        while symt is not None and symt.name != 'while' and symt.name != 'for':
            symt = symt.parent
        if symt is None:
            print('Break instruction outside of the loop in line ', node.line)

    '''def visit_LValue(self, node):
        lvalue = self.symtable.get(node.name)
        lvalue_type = self.symtable.get(node.name).type if lvalue is not None else None
        if node.indexes is not None:  # odwolujemy sie do jakiegos miejsca w macierzy
            if lvalue is None:   # macierz nie byla wczesniej zainicjalizowana
                print('Matrix was not yet initialized in line', node.line)
            elif not isinstance(lvalue_type, Matrix):  # zmienna nie jest macierza
                print("Variable is a scalar, can not be referenced as a matrix: {}".format(node.line))
            else:  # zmienna jest macierza
                if len(node.indexes) == 2:  # jesli odwolujemy sie do dwuwymiarowej macierzy
                    if lvalue_type.col_size is None:  # a macierz ma jeden wymiar
                        print('Referencing one dimensional matrix as a two dimensional in line', node.line)
                    else:  # a macierz ma dwa wymiary
                        if node.indexes[1] < 0 or node.indexes[1] >= lvalue_type.col_size:  # poza zakres macierzy
                            print('Referencing matrix out of bounds of column in line', node.line)
                if node.indexes[0] < 0 or node.indexes[0] >= lvalue_type.row_size :  # poza zakres macierzy
                    print('Referencing matrix out of bounds of row in line', node.line)
        return lvalue_type'''

    def visit_LValue(self, node):
        lvalue_type = self.symtable.get(node.name)
        if not isinstance(lvalue_type, Matrix) and len(node.indexes) != 0:
            print("Variable is not a matrix, can not be referenced as a matrix: {}".format(node.line))
        elif isinstance(lvalue_type, Matrix) and len(lvalue_type.scopes) < len(node.indexes):
            print("Matrix dimension is {}: {}".format(len(lvalue_type.scopes), node.line))
        elif isinstance(lvalue_type, Matrix):
            for i in range(len(node.indexes)):
                if lvalue_type.scopes[i] < node.indexes[i]:
                    print("Index out of bound: {}".format(node.line))
        return lvalue_type if len(node.indexes) == 0 else 'double'



    def visit_AssignmentInstr(self, node):
        node_type = self.visit(node.lvalue)
        expr_type = self.visit(node.expr)
        if node.op == '=':
            self.symtable.put(node.lvalue.name, expr_type)
            # self.symtable.put(node.lvalue.name, SymbolTable.VariableSymbol(node.lvalue.name, expr_type))
        else:
            if (node.op, node_type, expr_type) not in typemap.keys():
                print("Incompatible types for given operation: {}".format(node.line))
            self.symtable.put(node.lvalue.name, typemap[(node.op, node_type, expr_type)])

    def visit_WhileInstr(self, node):
        c_type = self.visit(node.cond)
        if c_type != 'int':
            print('Incorrect condition type in while instr in line ', node.line)
        self.symtable = self.symtable.pushScope('while')
        self.visit(node.instr)
        self.symtable = self.symtable.popScope()
            # self.symtable.put(node.lvalue.name, SymbolTable.VariableSymbol(node.lvalue.name, expr_type))


    def visit_IfElseInstr(self, node):
        c_type = self.visit(node.cond)
        if c_type != 'int':
            print('Incorrect condition type in if else instruction in line ', node.line)
        self.symtable = self.symtable.pushScope('if')
        self.visit(node.instr)
        self.symtable = self.symtable.popScope()
        if node.else_instr is not None:
            self.symtable = self.symtable.pushScope('else')
            self.visit(node.else_instr)
            self.symtable = self.symtable.popScope()

    def visit_ReturnInstr(self, node):
        self.visit(node.ret)

    def visit_PrintInstr(self, node):
        self.visit(node.to_print)

    def visit_PrintVarsList(self, node):
        for expr in node.print_list:
            self.visit(expr)

    def visit_InstrBlock(self, node):
        self.visit(node.instructions)

    def can_operate(self, m1: Matrix, m2: Matrix):
        if len(m1.scopes) == len(m2.scopes):
            for i in range(len(m1.scopes)):
                if self.visit(m1.scopes[i]) != self.visit(m2.scopes[i]):
                    return False
            return True
        return False

    def visit_BinOperation(self, node):
        type1 = self.visit(node.larg)
        type2 = self.visit(node.rarg)
        op = node.op
        if isinstance(type1, Matrix) and isinstance(type2, Matrix):
            if not (op, Matrix.__name__, Matrix.__name__) in typemap.keys():
                print("Not a valid operation for matrices in line ", node.line)
            elif not self.can_operate(type1, type2):
                print("Matrices sizes are not compilant in line: ",node.line)
            else:
                return type1
        elif (op, type1, type2) not in typemap.keys():
            print('Incompatible types in binary expression in line ', node.line)
            return None
        else:
            return typemap[(op, type1, type2)]

    def visit_EyeInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type is None or arg_type != 'int':
            print('Incorrect argument type in eye function in line: ', node.line)
            return None
        return Matrix([node.size, node.size])

    def visit_OnesInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type is None or arg_type != 'int':
            print('Incorrect argument type in ones function in line: ', node.line)
            return None
        return Matrix([node.size, node.size])

    def visit_ZerosInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type is None or arg_type != 'int':
            print('Incorrect argument type in zeros function in line: ', node.line)
            return None
        return Matrix([node.size, node.size])

    def visit_UnOperation(self, node):
        self.visit(node.arg)
        arg_type = self.symtable.get(node.arg)
        if arg_type is None:
            print("Variable ", node.arg, " undefined in line: ",node.line)
            return None
        elif arg_type != Matrix.__name__ and node.op == "'":
            print("Transposition operator on invalid type in line: ",node.line)
            return None
        return arg_type

    def visit_Matrix(self, node):
        for row in node.rows:
            self.visit(row)
        prev_size = None
        for row in node.rows:
            cur_size = len(row.row)
            if prev_size is not None and cur_size != prev_size:
                print('Incompatibile verctors size in line: ', row.line)
            prev_size = cur_size
        return Matrix([len(node.rows), len(node.rows[0].row)])
        # return Matrix(len(node.rows), len(node.rows[0].row))

    def visit_MatrixRow(self, node):
        prev_type = None
        for elem in node.row:
            elem_type = self.visit(elem)
            if prev_type is not None and prev_type != elem_type:
                print('Incompatibile types at initialization in line', node.line)
            prev_type = elem_type
