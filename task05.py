#5. **So‘zlar sonini hisoblash**
#**🧠 Vazifa**: Matn ichidagi har bir so‘z necha marta qatnashganini aniqlang. Natijani `dict` tarzida qaytaring.
#**➡️ Kirish**: `"salom salom dunyo"`#**⬅️ Chiqish**: `{'salom': 2, 'dunyo': 1}matn = input("Matnni kiriting: ")

matn = input("matnni kiriting: ")
sozlar = matn.split()
natija = {}

for soz in sozlar:
    if soz in natija:
        natija[soz] += 1
    else:
        natija[soz] = 1

print(natija)



