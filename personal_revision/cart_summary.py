item_number = int(input("How many items are you buying?"))

A = input("Enter name of item one: ")
AA = int(input("Enter price of item: "))

B = input("Enter name of item two: ") 
BB = int(input("Enter price of item: "))

C = input("Enter name of item three: ")
CC = int(input("Enter price of item: "))

discount_on_total_amount = 1500
total_amount = AA + BB + CC 


if total_amount > discount_on_total_amount:
    discount_rate = 0.03
else :
    discount_rate = 0

discounted_amount= discount_rate * total_amount
payable_amount = total_amount - discounted_amount


print("\n 🛒Your cart summary ")
print("-----------------")
print(f"{A} : KES {AA}")
print(f"{B} : KES {BB}")
print(f"{C} : KES {CC}")
print("-----------------")
print(f"TOTAL : KES {total_amount}")
print(f"discount you qualify for : KES {discounted_amount}")
print(f"final amount: KES {payable_amount}")
print("-----------------")
print("***Thank You For Shoppping With Us***")