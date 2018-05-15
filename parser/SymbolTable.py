

class VariableSymbol(object):

    def __init__(self, name, type):
        pass
    #


class SymbolTable(object):

    def __init__(self, parent, name):  # parent scope and symbol table name
        self.parent = parent
        self.name = name

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        pass

    def get(self, name):  # get variable symbol or fundef from <name> entry
        pass

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        pass

    def popScope(self):
        pass
