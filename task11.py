import json

with open("Input/students.json") as jsonfayl:
    students = json.load(jsonfayl)

soni = len(students)

with open("Output/output11.json", "w") as jsonfile:
    json.dump({"count": soni}, jsonfile, indent=4)
