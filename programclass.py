from class_class import MyClass

class Program:
    def __init__(self, name):
        self.name = name
        self.allmyclasses = []

    def addclass(self, classname, attributes = [], methods = []):
        newclass = MyClass(classname)
        self.allmyclasses.append(newclass)
        for aattribute in attributes:
            newclass.addattribute(aattribute[0], aattribute[1])
        for amethod in methods:
            newclass.addmethod(amethod[0],amethod[1])

    def printprogram(self):
        for aclass in self.allmyclasses:
            aclass.printclass()