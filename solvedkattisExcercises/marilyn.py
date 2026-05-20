import random

rounds = 1000
doors = ["A","B","C"]

for _ in range(rounds):
    remainingDoors = doors.copy()

    guess = random.choice(doors)
    print(guess)

    remainingDoors.remove(guess)

    response = input().split(" ")
    door = response[0]

    bottleOrNot = response[1]

    if bottleOrNot == "1":
        finalGuess = door
    else:
        remainingDoors.remove(door)
        finalGuess = random.choice(remainingDoors)
    

    print(finalGuess)

    result = input()


  