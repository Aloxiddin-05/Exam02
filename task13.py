import json

with open("Input/students.json", "r") as jsonfayl:
    students = json.load(jsonfayl)

uzun_ismlar = []
for student in students:
    ism = student["name"]             
    if len(ism) > 5:                  
        uzun_ismlar.append(ism)     

with open("Output/output13.json", "w") as jsonfayl:
    json.dump({"uzun names": uzun_ismlar}, jsonfayl, indent=4)
