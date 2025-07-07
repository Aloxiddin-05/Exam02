#4. **FISH tartibini o‘zgartirish**
#Vazifa: Foydalanuvchi FISH (Familiya Ism Sharif) kiritadi. Siz uni `Ism Sharif, Familiya` shaklida chiqarishingiz kerak.
#**➡️ Kirish**: `"Aliyev Vali G'aniyevich"`
#**⬅️ Chiqish**: `"Vali G'aniyevich, Aliyev"`

fish = input("FISHni kiriting: ")

elementlari = fish.split()

if len(elementlari) >= 3:
    familiya = elementlari[0]
    ism_sharif = " ".join(elementlari[1:])
    print(f"{ism_sharif} {familiya}")
else:
    print("Noto‘g‘ri format")



