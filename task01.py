def add(a, b):
    return a + b
    
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b

def main():
    a = float(input("a = "))
    amal = input("`+`, `-`, `*`, `/`  kiriting: ")
    b = float(input("b = "))
    
    
    if amal == "+":
        print(add(a,b))
    elif amal == "-":
        print(subtract(a,b))
    elif amal == "/":
        if b == 0:
            print("nol kiritish mumkin emas")
        else:
            print(divide(a,b))
    elif amal == "*":
        print(multiply(a,b))
        
    
main()