class Attribute:
    def __init__(self, parentclass,  name, type):
        self.parentclass = parentclass
        self.name = name
        self.type = type

    def printattribute(self):
        print(self.name, ": ", self.type)