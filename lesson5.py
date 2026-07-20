# A countdown using a while loop (When you dont know thew end point of the loop)
count = 4

while count > 0:
    print(count)
    count -= 1

print("Blast off!")


# Building a simple  rep counter using a while loop (When you know the end point of the loop)
for rep in range(1, 4):
    print(f"This is rep no. {rep}")



# A guessing game


secrete_word = "python"

while True:
    gueess = input("Guess the programming language we are using: ").lower().strip()

    if gueess == secrete_word:
        print("You guessed it right!")
        break
    else:
        print("Try again!")
        gueess = input("Guess the programming language we are using: ").lower().strip()