import json


with open("Input/students.json") as jsonfayl:
    students = json.load(jsonfayl)

ismlar = []
for student in students:
    ism = student["name"]     
    ismlar.append(ism)        
    
ismlar.sort()

with open("Output/output12.json", "w") as jsonfayl:
    json.dump({"sorted_names": ismlar}, jsonfayl, indent=4)
