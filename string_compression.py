""" system module."""


def compress():
    user = input("ENTER AN INPUT : ")
    user = user.upper()
    u_len = len(user)
    x_r = u_len
    while not user.isalpha():
        print(" INVALID INPUT  :(")
        compress()
    print("your input string is:", user)
    count = 1
    opt = []
    i = 1
    while i < u_len:
        if user[i] == user[i - 1]:
            count += 1
        else:
            if count <= 1:
                opt.append(user[i - 1])
                count = 1
            else:
                opt.append(str(count) + user[i - 1])
                count = 1
        i += 1
    if count <= 1:
        lstr = str(user[i - 1])
    else:
        lstr = str(count) + user[i - 1]
    opt.append(lstr)
    result = ''
    for i in opt:
        result += i
    print("your compressed string is: ", result)
    y_r = len(result)
    print("the compression ratio is =", x_r, ':', y_r)
    comp = input("do you want to  continue the compression: ")
    comp = comp.upper()
    while True:
        if comp == 'YES':
            compress()
        elif comp == 'NO':
            print("THANK YOU! Have a nice day! :)")
            exit()
        else:
            print("INVALID INPUT :(")
            comp = input("enter yes/no : ")
            comp = comp.upper()


compress()
