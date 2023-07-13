name = str (input("Enter name"))
age =  int (input("Enter age"))

ages = ""

if age >= 18:
    ages = "คุณเป็นผู้ใหญ่"

elif age >= 13 and age <= 17:
    ages = "คุณเป็นเด็กวัยรุ่น"
elif age >= 6 and age <= 12:
    ages = "คุณเป็นเด็ก"
elif age < 6:
    ages = "คุณเป็นเด็กแรกเกิด"

print("คุณชื่อ ",name,"อายุของคุณ",age,' ',ages)



