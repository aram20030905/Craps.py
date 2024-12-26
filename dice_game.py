import random

while True:
    oneNumber=random.randrange(1,7)
    twoNumber=random.randrange(1,7)
    generalsum=oneNumber+twoNumber
    print("The sum of dice is"+" "+str(oneNumber) + " + " + str(twoNumber) + " = " + str(generalsum))

    if generalsum == 7 or generalsum == 11:
        print("You won")
        break

    elif generalsum == 2 or generalsum == 3 or generalsum == 12:
        print("You lost")
        break

    elif generalsum in {4,5,6,8,9,10}:
        goal = generalsum
        print("Now your goal number is"+" "+str(goal))

        while True:
            oneNumber = random.randrange(1,7)
            twoNumber = random.randrange(1,7)
            generalsum = oneNumber + twoNumber
            print("The sum of dice is"+" "+str(oneNumber) + " + " + str(twoNumber) + " = " + str(generalsum))
            if generalsum == goal:
                print("You won")
                break

            elif generalsum == 7:
                print("You lost")
                break

        break


        


