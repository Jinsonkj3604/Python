lines = int(input("how many lines you want: "))
print("your input number is:", lines)
lmt = 1
for i in range(1, lines+1):
    for j in range(2):
        if lmt < lines+1:
            k = i*2
            print(" "*(lines-i), "*"*k , " "*(lines-i))
            lmt += 1
        else:
            break



