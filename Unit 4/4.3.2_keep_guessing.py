import random

my_num = random.randrange(1, 11)
choice = int(input("I am thinking of a number from 1-10. Pick a number. \n"))
run = True

while run:
    if my_num == choice:
        print(f"Congratulations. I was thinking of {my_num}\n")
        exit()
        run = False
    else:
        choice = int(input("Incorrect. Guess again. \n"))