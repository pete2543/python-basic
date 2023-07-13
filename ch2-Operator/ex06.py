amount = input("Enter amount")
rate = input(" Enter rate")
year = input("Enter year")


amount_1 = int(amount)
rate_2 = float(rate)
year_3 = int(year)

total = amount_1*(1 + rate_2/100)**year_3

print("Enter amount",amount_1)
print("Enter rate",rate_2)
print("Enter yaer",year_3)
print("value",total)

