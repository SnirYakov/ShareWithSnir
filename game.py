import random as rd

tries= 5
counter= 0
secret_number= rd.randint(0, 20)
guess= input("please enter your guess: ")

while not guess.isdigit():
    guess= input("this is not a valid number, please try again")
guess= int(guess)
while guess != secret_number:
    if guess < secret_number:
        print(guess, "too low")
    else:
        print(guess, "too high")
    counter= counter+1
    if counter == tries:
        break
    guess = int(input("try again"))
if counter <tries:
    print ("congratulations, you won!")
elif counter <tries and counter== 1:
    print("wow!!!!! you supper lucky!!!")
else:
    print("you used all of your tries sorry.. the correct answer is",guess)
    print("you lose!")
 