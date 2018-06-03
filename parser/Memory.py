
class Memory:

    def __init__(self, name): # memory name
        self.name = name
        self.mem = {}

    def get(self, name):         # gets from memory current value of variable <name>
        return self.mem[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.mem[name] = value


class MemoryStack:

    def __init__(self, memory=None): # initialize memory stack with memory <memory>
        self.stack = [memory] if memory is not None else [Memory('global')]

    def get(self, name): # gets from memory stack current value of variable <name>
        stack_depth = len(self.stack)
        i = stack_depth - 1
        found = False
        ret = None
        while not found and i >= 0:
            found = name in self.stack[i].mem
            if found:
                ret = self.stack[i].get(name)
            i -= 1
        return ret

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.stack[len(self.stack) - 1].put(name, value)

    def set(self, name, value):     # sets variable <name> to value <value>
        for mem in self.stack:
            if name in mem:
                mem.put(name, value)

    def push(self, memory):     # pushes memory <memory> onto the stack
        self.stack.append(memory)

    def pop(self):          # pops the top memory from the stack
        return self.stack.pop()
