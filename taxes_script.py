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

def calculate_quebec_tax(income):
    quebec_tax = 0
    
    if income > 140000:
        quebec_tax += (income - 140000) * 0.30
        income = 140000
    if income > 107838:
        quebec_tax += (income - 117850) * 0.24
        income = 117850
    if income > 98540:
        quebec_tax += (income - 98540) * 0.20
        income = 98540
    if income > 49275:
        quebec_tax += (income - 49275) * 0.15
        income = 49275
    
    provincial_tax += income * 0.0505
    
    return provincial_tax

quebec_tax = calculate_quebec_tax(annual_income)
print(f"Provincial Tax (Quebec): ${quebec_tax:.2f}")