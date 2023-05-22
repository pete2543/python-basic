
money = float(input("Enter number money withdraw :" ))

print ("Cash B1000 :", money/1000)
print ("Cash B500 :", (money%1000)/500)
print ("Cash B100 :", ((money%1000)%500)/100)