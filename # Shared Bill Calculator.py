# Shared Bill Calculator
# This program calculates how much each person has to pay
# based on rent, food, and electricity consumption.

# Input from user
rent = int(input("Enter your hostel/flat rent:"))
food = int(input("Enter the amount of food ordered :"))
electricity_units =int(input("Enter the total of electricity unit: "))
charge_per_unit = int(input("Enter the charge per unit :"))

# Calculate total bill per person 
persons = int(input("Enter the number of persons living in room/flat:"))
total_bill = electricity_units * charge_per_unit 
output = (food + rent + total_bill )//persons
# Out put 
print("Each person will pay =" , output )