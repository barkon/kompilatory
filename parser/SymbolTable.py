

class VariableSymbol(object):

    def __init__(self, name, type):
        pass
    #


class SymbolTable(object):

    def __init__(self, parent, name):  # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.entries = {}
        self.scopes = {}

    def put(self, name, symbol):  # put variable symbol or fundef under <name> entry
        self.entries[name] = symbol

    def put_scope(self, name, indexes):
        self.scopes[name] = indexes

    def get(self, name):  # get variable symbol or fundef from <name> entry
        if name in self.entries.keys():
            return self.entries[name]
        elif self.parent is None:
            return None
        else:
            return self.parent.get(name)

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        new_scope = SymbolTable(self, name)
        self.entries[name] = new_scope
        return new_scope

    def popScope(self):
        parent_scope = self.getParentScope()
        if parent_scope is None:
            print('Cannot pop root scope')
        parent_scope.pop(self.name)
        return parent_scope
