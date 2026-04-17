"""
Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a
 medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75,
 then allowed; otherwise, not allowed."""
a=input("Enter if you have a medical condition ")
if a=="yes":
    print("You can take the exam.")
else:
    b=int(input("Enter your attendance "))
    if b>=75:
        print("You can take the exam.")
    else:
        print("You can not take the exam.")