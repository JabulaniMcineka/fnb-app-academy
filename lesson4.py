# Basic if/else script

age = int(input("Enter your age: "))


section_pass =  input("Have you passed the section test? (yes/no): ").lower().strip()



if age >= 18 and section_pass == "yes":
    print("Access grantered to the VIP section !!!") #green light priority
elif age >= 18:
    print("Access grantered to the general section!!!") #green light
else:
    print("Access denied !!!") #red light
