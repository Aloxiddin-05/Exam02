with open("Input/grades.csv") as csvfayl:
    qatorlar = csvfayl.read().splitlines()

qatorlar.pop(0)

beshliklar_soni = 0

for qator in qatorlar:
    if qator.strip():
        name, grade = qator.split(",")
        if int(grade) == 5:
            beshliklar_soni += 1

with open("Output/output16.txt", "w") as txtfile:
    txtfile.write(f"5 baho olganlar soni: {beshliklar_soni}")
