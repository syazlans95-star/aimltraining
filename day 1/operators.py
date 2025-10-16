phyMarks=int(input("Enter marks obtained in physic"))
cheMarks=int(input("Enter mark obtained in Chemistry"))
mathMarks=int(input("Enter mark obtained in Mathematics"))

if((mathMarks>=50) and (phyMarks>=55) and (cheMarks>=60)):
        print("You are eligible to sit in pre exam of MBSS")
else:
        print("You have not got the required marks")

