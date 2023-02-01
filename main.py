import random
import sys
odpowiedz = random.randint(0, 100)
print("Welcome")
print("Im thinking of a number of 1 to 100")
# print(f"Psst the correct answer is {odpowiedz} ")
attempts = 0



def game():
    global attempts
    game_state = True
    level = input("choose difficulty 'easy' or 'hard'")
    if level == "hard":
        attempts = 2
    elif level == "easy":
        attempts = 3
    else:
        print("nie ma takiego levelu ")
        sys.exit()
    print(f"You have {attempts} attempts left")

    while game_state:
        zgaduj = int(input("Make a guess: "))
        if zgaduj == odpowiedz:
            print("You won")
            game_state = False
            break
        if zgaduj > odpowiedz:
            attempts -= 1
            if attempts == 0:
                print("You lost")
                game_state = False
                break
            else:
                print("Too high")
                print("Guess again")
                print(f"You have {attempts} attempts left")
        if zgaduj < odpowiedz:
            attempts -= 1
            if attempts == 0:
                print("You lost")
                game_state = False
                break
            else:
                print("Too low")
                print("Guess again")
                print(f"You have {attempts} attempts left")


game()
