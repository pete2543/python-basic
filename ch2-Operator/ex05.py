import math

fnum = float(input("Enter float numner :"))


print()
print("Ceil number :",math.ceil (fnum))
print("Floor number :",math.floor(fnum))
print("Sqrt number :",math.trunc(fnum))

num = math.trunc(fnum)
print("Degree Angle :", num)
print("Redians Angle :",math.redians(num))
print("sin  :",math.sin(math.redians(num)))
print("cos  :",math.cos(math.redians(num)))
print("tan  :",math.tan(math.redians(num)))


