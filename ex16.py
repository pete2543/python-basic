Done = True
Count = 0
while Done :
     Score = input(f"Enter score value #{Count+1}: ")
     if Score != "-1":
         Mark = float(Score)
         if Mark >=0 and Mark <=100 :
            Grade = ""
            if Mark >=80:
                Grade = "A"
            elif Mark >= 75 and Mark <= 79 :
                 Grade = "B+"
            elif Mark >= 70 and Mark <= 74 :
                 Grade = "B"
            elif Mark >= 65 and Mark <= 69 :
                 Grade = "c+"
            elif Mark >= 60 and Mark <= 64 :
                 Grade = "c"
            elif Mark >= 55 and Mark <= 59 :
                 Grade = "D+"
            elif Mark >= 50 and Mark <= 54 :
                 Grade = "D"
            else:
                 Grade = "F"
            print(f"Score is {Mark}, get {Grade}")
         else:
            print("Score out of rang, input again.")
     elif Score == "-1":
         Done = False
print("Exit Program")
