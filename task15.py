with open("Input/grades.csv") as csvfile:
    qatorlar = csvfile.read().splitlines()

qatorlar.pop(0)

eng_yuqori_baho = -1
eng_yaxshi_talaba = ""

for qator in qatorlar:
    if qator.strip():
        name, grade = qator.split(",")
        grade = int(grade)

        if grade > eng_yuqori_baho:
            eng_yuqori_baho = grade
            eng_yaxshi_talaba = name

with open("Output/output15.txt", "w") as txtfile:
    txtfile.write(f"Bahosi eng yuqori o‘quvchi: {eng_yaxshi_talaba} - {eng_yuqori_baho}")
