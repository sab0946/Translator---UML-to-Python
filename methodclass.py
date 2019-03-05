class Method:
    def __init__(self, parentclass,  name, output):
        self.parentclass = parentclass
        self.name = name
        self.output = output

    def printmethod(self):
        print(self.name, "(): ", self.output)