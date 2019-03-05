from attributeclass import Attribute
from methodclass import Method
from relationshipclass import Relationship

class MyClass:
    def __init__(self, name):
        self.name = name
        self.allmyattributes = []
        self.allmymethods = []
        self.allmyrelationships = []

    def addattribute(self, aname, atype):
        newattribute = Attribute(self, aname, atype)
        self.allmyattributes.append(newattribute)

    def addmethod(self, mname, mtype):
        newmethod = Method(self, mname, mtype)
        self.allmymethods.append(newmethod)

    def addrelationship(self, arelationship):
        newrelationship = Relationship(arelationship)
        self.allmyrelationships.append(arelationship)

    def printclass(self):
        print(self.name)
        print("________")
        for aattirbute in self.allmyattributes:
            aattirbute.printattribute()
        print("________")
        for amethod in self.allmymethods:
            amethod.printmethod()
        print("________")
        for arelationship in self.allmyrelationships:
            arelationship.printrelationship()