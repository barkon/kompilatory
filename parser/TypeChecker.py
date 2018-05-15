import AST
import SymbolTable

typemap = dict()
for op in ['+', '-', '/', '*']:
    typemap[(op, 'int', 'int')] = 'int'
    typemap[(op, 'float', 'float')] = 'float'
    typemap[(op, 'int', 'float')] = 'float'
    typemap[(op, 'float', 'int')] = 'float'

for io in ['>', '<', '==', '!=', '>=', '<=']:
    typemap[(op, 'int', 'int')] = 'int'
    typemap[(op, 'float', 'float')] = 'int'
    typemap[(op, 'int', 'float')] = 'int'
    typemap[(op, 'float', 'int')] = 'int'

for op in ['.+', '.-', './', '.*']:
    typemap[(op, 'matrix', 'matrix')] = 'matrix'


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
        self.root_table = SymbolTable.SymbolTable(None, 'root')

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
        type1 = self.visit(node.left)  # type1 = node.left.accept(self)
        type2 = self.visit(node.right)  # type2 = node.right.accept(self)
        op = node.op
        op_type = typemap[(op, type1, type2)]
        if op_type is None:
            print('Incompatible types in binary expression in line:')
        return op_type

    def visit_Variable(self, node):
        pass


