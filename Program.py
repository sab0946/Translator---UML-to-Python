## import class modules
from programclass import Program

x = Program("TestOne")
x.addclass("FirstClass", [["firstAttribute", "string"], ["secondAttribute", "null"]],
           [["firstMethod", "boolean"]])
x.addclass("SecondClass", [["anotherAttribute", "integer"]],
           [["otherMethod", "string"], ["nextMethod", "number"]])

x.printprogram()







