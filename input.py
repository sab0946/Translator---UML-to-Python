## import class modules
from programclass import Program

class InterpretClass:
    def __init__(self, newinput):
        self.input = newinput
        self.foundclass = []
        self.allfoundmethods = []
        self.allfoundattributes = []

    def interpretfile(self):
        newprogram = Program(x[0])
        for line in x:
            if line.count("-") == 1:
                newclass = line.replace("-", "")
                self.foundclass.append(newclass)
            for line in x:
                if line.count("-") == 2:
                    newattribute = line.replace("-", "")
                    self.allfoundattributes.append(newattribute.split(" "))
                elif line.count("-") == 3:
                    newmethod = line.replace("-", "")
                    self.allfoundmethods.append(newmethod.split(" "))


with open('input.txt') as file:
    file_contents = file.read()
    x = file_contents.splitlines()
    newprogram = x[0]
    classsplit = x.index["newclass"]
    classinfo = []
    i = 1
    while i < classsplit:
        firstclass.append(x[i])
        x.pop(x[i])


    #classlist = x
    #print(classlist)

    #for classes in classlist:
        #interpret = InterpretClass(classes)
        #interpret.interpretfile()
        #print(interpret.foundclass)
        #print(interpret.allfoundattributes)
        #print(interpret.allfoundmethods)
