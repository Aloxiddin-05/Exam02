with open("Input/numbers.txt") as fayl:
    matn = fayl.read()
    sonlar = list(map(int, matn.split()))

sonlar.sort()

with open("Output/output10.txt", "w") as natija:
    for son in sonlar:
        natija.write(f"{son}\n")
