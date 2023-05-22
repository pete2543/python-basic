amout = float(input("Enter amout :"))
rate  = float(input("Enter rate :"))
year  = float(input("Enter year :"))
rate2 = rate/100
num = (amout*((1+rate2)**year))

print ("future value",num)