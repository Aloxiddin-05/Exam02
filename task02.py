def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Mablag' yetarli emas!")
        return balance
    return balance - amount

def check_balance(balance):
    return balance

def main():
    balance = 0

    while True:
        print("\nBu Sizning elektron xamyoningiz")
        print("1. Balansni tekshirish")
        print("2. Pul chiqarish")
        print("3. Pul to‘ldirish")
        print("4. Dasturdan chiqish")

        menyu = input("Nima qilamiz (1-4): ")

        if menyu == "1":
            print(f"Balansingiz: {check_balance(balance)} $ so'm")
        elif menyu == "2":
            amount = float(input("Yechiladigan summani kiriting: "))
            balance = withdraw(balance, amount)
            print(f"Yangi balans: {balance} so'm")
        elif menyu == "3":
            amount = float(input("Qo‘yiladigan summani kiriting: "))
            balance = deposit(balance, amount)
            print(f"Yangi balans: {balance} so'm")
        elif menyu == "4":
            print("Dasturdan chiqilmoqda")
            break
        else:
            print("Menyuni noto'g'ri kiritdinggiz 1-4 oralig‘ida tanlang.")

main()

    