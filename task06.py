students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}

ortalacha = sum(students.values()) / len(students)

yuqorilar = []
for ism, baho in students.items():
    if baho > ortalacha:
        yuqorilar.append(ism)

print("O‘rtacha baho:", round(ortalacha, 2))
print(f"{round(ortalacha, 2)} dan yuqorilar:", ", ".join(yuqorilar))


    

    