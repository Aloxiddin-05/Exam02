with open("Input/numbers.txt") as fayl:
    matn = fayl.read()
    sonlar = list(map(int, matn.split()))

eng_katta = max(sonlar)

with open("Output/output09.txt", "w") as natija:
    natija.write(f"Eng katta son: {eng_katta}")
