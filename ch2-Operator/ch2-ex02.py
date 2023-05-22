number= int(input("Enter integer number :"))
a= (number%10000)/1000
b= ((number%10000)%1000)/100
c= ((number%10000)%1000%100)/10
d= ((number%10000)%1000%100%10)/1
print(round(a))
print (round(b))
print (round(c))
print (round(d))  