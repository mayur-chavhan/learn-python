print("Thank you for choosing Python Pizza Deliveries!")

size = input('What size pizza do you want? "S", "M", or "L": ')
# What size pizza do you want? "S", "M", or "L"
add_pepperoni = input('Do you want pepperoni? "Y" or "N": ')
# Do you want pepperoni? "Y" or "N"
extra_cheese = input('Do you want extra cheese? "Y" or "N": ')
# Do you want extra cheese? "Y" or "N"

total_bill = 0

if size == "S":
  total_bill += 15
elif size == "M":
  total_bill += 20
else:
  total_bill += 25

if add_pepperoni == "Y":
  if size == "S":
    total_bill += 2
  else:
    total_bill += 3

if extra_cheese == "Y":
  total_bill += 1

print(f"\nYour final bill is: ${total_bill}.")
exit(0)

#Technique 2: Using Dictionaries for Pricing
#This method uses dictionaries to store prices, making it easier to update or modify prices.

# print("Thank you for choosing Python Pizza Deliveries!")

# size = input('What size pizza do you want? "S", "M", or "L": ').upper()
# add_pepperoni = input('Do you want pepperoni? "Y" or "N": ').upper()
# extra_cheese = input('Do you want extra cheese? "Y" or "N": ').upper()

# # Dictionaries to hold prices
# size_prices = {"S": 15, "M": 20, "L": 25}
# pepperoni_prices = {"S": 2, "M": 3, "L": 3}
# cheese_price = 1

# # Initialize cost with base price
# cost = size_prices.get(size, 0)

# # Add pepperoni cost if selected
# if add_pepperoni == "Y":
#     cost += pepperoni_prices[size]

# # Add cheese cost if selected
# if extra_cheese == "Y":
#     cost += cheese_price

# print(f"The total cost of your pizza is: ${cost}")
