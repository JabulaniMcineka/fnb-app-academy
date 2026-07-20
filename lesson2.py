# Tracking indivisual letters
name = "Python"
print(name[0])  # Output: P
print(name[1])  # Output: y
print(name[2])  # Output: t
print(name[3])  # Output: h
print(name[4])  # Output: o
print(name[5])  # Output: n


# using string methods
town = "  Johannesburg  "
print(town.upper())  # Output: JOHANNESBURG
print(town.lower())  # Output: johannesburg 
print(town.strip())  # Output: Johannesburg (removes leading/trailing whitespace)


# Creating a proffessional systsem generator
first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username = f"{first[0]}{last}"

print(f"your email address is: {username.lower()}@fnb.co.za")