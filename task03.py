def calculate_tax(salary):
    if salary > 5_000_000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return int(tax)

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    net_salary = salary - tax
    return int(net_salary)

salary = float(input("salary = "))
tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)

print("Soliq:", tax)
print("Sof maosh:", net_salary)
