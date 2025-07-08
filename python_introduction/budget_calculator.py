#usr input 
monthly_income = int(input("what is your total monthly income?"))

prompt= input("Enter how much you spend on the following:")

rent = int(input("rent: "))
food = int(input("food: "))
transport = int(input("transport: "))
utilities = int(input("utilities: "))
entertainement = int(input("entertainement: "))

categories = [rent,food, transport,utilities, entertainement]

#compute expenses and balance
expenses = rent + food + transport + utilities + entertainement
remaining_balance = monthly_income - expenses

#category breakdown
A = rent/monthly_income * 100
B = food/monthly_income * 100
C = transport/monthly_income * 100
D = utilities/monthly_income * 100
E = entertainement/monthly_income * 100


#print out results 
print(f"the breakdown of your spend is as follows: rent: {A}%,food: {B}%,transport: {C}%,utilities: {D}%,entertainment: {E}%.Your total expenses are KES {expenses}  , and your remaining balance after deductions is KES{remaining_balance}")


if A > monthly_income or B > monthly_income or C > monthly_income or D > monthly_income or E > monthly_income:
    print("You are overspending!")
else:
    print("You are within the budget")



