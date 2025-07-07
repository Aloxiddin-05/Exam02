with open("Input/numbers.txt") as fayl:
    matn = fayl.read()
    sonlar = matn.split()

yigindi = 0

for son in sonlar:
    son = int(son)   
    yigindi += son   

with open("Output/output08.txt", "w") as chiqish:
    chiqish.write(f"Yig'indi: {yigindi}")

