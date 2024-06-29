annual_income = float(input("Enter your annual income: "))

def calculate_federal_tax(income):
    federal_tax = 0
    
    if income > 234609:
        federal_tax += (income - 234609) * 0.33
        income = 234609
    if income > 164914:
        federal_tax += (income - 164914) * 0.29
        income = 164914
    if income > 106717:
        federal_tax += (income - 106717) * 0.26
        income = 106717
    if income > 53359:
        federal_tax += (income - 53359) * 0.205
        income = 53359
    
    federal_tax += income * 0.15
    
    return federal_tax

print(f"Federal Tax: ${federal_tax:.2f}")