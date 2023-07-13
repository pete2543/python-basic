import math
money = float(input("Enter number money withdraw :" ))

print ("Cash B1000 :", math.floor(money/1000)%1000)
print ("Cash B500 :", math.floor(money%1000/500))
print ("Cash B100 :", math.floor(money%1000)%500/100)