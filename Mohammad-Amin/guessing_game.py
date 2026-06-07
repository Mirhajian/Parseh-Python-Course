import random as r

def guess(s, g, mr):
    game = "Game Over"
    state = False
    while(state == False and mr > 0):
    
        print(f"You have {mr} retry")
        mr = mr - 1
    
        if g == s:
            state = True
            game = "Victory"
            return game
        elif g > s:
            g = int(input("Your number is higher, try again: "))
        else:
            g = int(input("Your number is lower, try again: "))

    return game


max_retry = 5
secret = r.randint(1, 20)
guess_number = int(input("Guess what i am thinking of: "))

final = guess(secret, guess_number, max_retry)

if final == "Victory":
    print("You won!")
else:
    print("You lost, my number was:", secret)
