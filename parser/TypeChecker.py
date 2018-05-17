import AST
import SymbolTable

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

for op in ['+=', '-=', '*=', '/=']:
    typemap[(op, 'int', 'int')] = 'int'
    typemap[(op, 'float', 'float')] = 'float'
    typemap[(op, 'int', 'float')] = 'float'
    typemap[(op, 'float', 'int')] = 'float'


class Matrix:
    def __init__(self, row_size, col_size):
        self.row_size = row_size
        self.col_size = col_size


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

    def visit_ForInstr(self, node):
        self.visit(node.for_init)
        self.symtable = self.symtable.pushScope('for')
        self.visit(node.instr)
        self.symtable = self.symtable.popScope()

    def visit_ForInit(self, node):
        fr_type = self.visit(node.fr)
        to_type = self.visit(node.to)
        if fr_type == 'string' or to_type == 'string':
            print("String is nor a valid type for for init in line: ", node.line)
        elif fr_type != to_type:
            print("Incompatible types at for init in line: ", node.line)

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

    def visit_AssignmentInstr(self, node):
        node_type = self.visit(node.lvalue)
        expr_type = self.visit(node.expr)
        if node.op == '=':
            self.symtable.put(node.lvalue.name, SymbolTable.VariableSymbol(node.lvalue.name, expr_type))
        else:
            if (node.op, node_type, expr_type) not in typemap.keys():
                print("Incompatible types for given operation: {}".format(node.line))
            self.symtable.put(node.lvalue.name, SymbolTable.VariableSymbol(node.lvalue.name, expr_type))

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

    def visit_LValue(self, node):
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
        return lvalue_type

    def visit_ReturnInstr(self, node):
        self.visit(node.ret)

    def visit_PrintInstr(self, node):
        self.visit(node.to_print)

    def visit_PrintVarsList(self, node):
        for expr in node.print_list:
            self.visit(expr)

    def visit_InstrBlock(self, node):
        self.visit(node.instructions)

    def visit_BinOperation(self, node):
        type1 = self.visit(node.larg)
        type2 = self.visit(node.rarg)
        op = node.op
        if (op, type1, type2) not in typemap.keys():
            print('Incompatible types in binary expression in line ', node.line)
            return None
        else:
            return typemap[(op, type1, type2)]

    def visit_EyeInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type != 'int':
            print('Incorrect argument type in eye function in line:')
        return Matrix(node.size, node.size)

    def visit_OnesInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type != 'int':
            print('Incorrect argument type in ones function in line:')
        return Matrix(node.size, node.size)

    def visit_ZerosInit(self, node):
        arg_type = self.visit(node.size)
        if arg_type != 'int':
            print('Incorrect argument type in zeros function in line:')
        return Matrix(node.size, node.size)

    def visit_UnOperation(self, node):
        self.visit(node.arg)
        arg_type = self.symtable.get(node.arg)
        if arg_type is None:
            print("Variable ", node.arg, " undefined in line: ",node.line)
        elif arg_type != 'matrix' and node.op == "'":
            print("Transposition operator on scalar in line: ",node.line)

    def visit_Matrix(self, node):
        for row in node.rows:
            self.visit(row)
        prev_size = None
        for row in node.rows:
            if prev_size is not None and len(row.row) != prev_size:
                print('Incompatibile vectors size in line: ', row.line)
            prev_size = len(row.row)
        return Matrix(len(node.rows), len(node.rows[0].row))

    def visit_MatrixRow(self, node):
        prev_type = None
        for elem in node.row:
            elem_type = self.visit(elem)
            if prev_type is not None and prev_type != elem_type:
                print('Incompatibile types at initialization in line', node.line)
            prev_type = elem_type
