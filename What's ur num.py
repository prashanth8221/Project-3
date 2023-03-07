import random

print("WHAT'S YOUR NUMBER")
n=random.randrange(1,100)
guess=int(input(""))
while n!=guess:
    if guess>n:
        print("Too High")
        guess=int(input(''))
    elif guess<n:
        print('Too low')
        guess=int(input(" "))
print('yes u guessed')

