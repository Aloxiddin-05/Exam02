import json

with open("Input/students.json", "r") as jsonfayl:
    students = json.load(jsonfayl)

a_harflilar = []

for student in students:
    ism = student["name"]         
    if ism.startswith("A"):        
        a_harflilar.append(ism)     

with open("Output/output14.json", "w") as jsonfile:
    json.dump({"a_names": a_harflilar}, jsonfile, indent=4)
