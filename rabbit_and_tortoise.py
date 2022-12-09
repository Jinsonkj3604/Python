import random


def generate():
    global cnum
    n = random.randint(0000, 10000)
    cnum = str(n).zfill(4)
    print("system generate number:", cnum)
    guess()
def guess():
    point1 = 0
    point2 = 0
    w = 0
    x = 0
    gnum = input("enter your 4 digit guess number: ")

    while len(gnum)!=4:
        print("invalid input!! must include 4 digits")
        gnum = input("enter 4 digit number: ")

    while not gnum.isdigit():
        print("invalid input!! only include digits")
        gnum = input("enter 4 digit number: ")

    if gnum == cnum:
        print("you win")
        w = 1
        x=1

    elif cnum != gnum:
        x=0
        for i in range(4):
            if cnum[i] == gnum[i]:
                point1 = point1 + 1
                x=1
            elif gnum[i] in cnum:
                point2 = point2 + 1
                x = 1
        print("you got", point1 ,"rabbit")
        print("you gpot", point2, "tortoise")

        if x == 0:
            print("you lose!!")

    while True:
        print("do you want to continue!")
        again = input("enter yes/no ")
        again = again.lower()
        while again != 'yes' and again != 'no':
            print("invalid input!!")
            again= input("enter yes or no: ")
        if again == 'yes' and w == 1:
                generate()
        elif again == 'yes':
            print("generated number is ", cnum)
            guess()
        else:
            quit()
generate()


