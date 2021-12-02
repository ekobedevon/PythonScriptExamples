
import random

print("hello")
random.seed(0)
answer = random.randrange(1,10)
print(answer)
guess = 10

for x in range(guess):
    player_ans = input("Enter a number: ")
    if player_ans is answer:
        print("Good job")
        break
    elif player_ans is not answer:
        print("You are wrong")