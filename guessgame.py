import random
num = random.randint(1,10)
temp = input("input number:")
guess = int(temp)
if guess == num:
    print("you are right. game over.")
while guess != num:
    temp = input("wrong.input again:")
    guess = int(temp)
    if guess == num:
        print("you are right.")
    else:
        if guess < num:
            print("small.")
        else:
            print("big.")
