#user input 
monthly_salary = int(input("Enter your monthly salary: " ))
annual_salary = monthly_salary * 12 


#conditional loops for various tax brackets 
if annual_salary <= 288000:
    tax_rate = 0.10
elif annual_salary <= 500000:
    tax_rate = 0.20
elif annual_salary <= 1000000:
    tax_rate = 0.30
else:
    tax_rate = 0.35
    
    
tax_amount = annual_salary * tax_rate
net_annual_salary = annual_salary - tax_amount
net_monthly_salary = net_annual_salary/12 

print("\n Your details are as follows:")
print("--------------------------------")
print(f"Your annual salary is: KES {annual_salary}")
print(f"Your total tax amount is: KES {tax_amount} ")
print(f"Your net annual salary after tax is  is: KES {net_annual_salary} ")
print(f"Your net monthly salary  is: KES {net_monthly_salary} ")







