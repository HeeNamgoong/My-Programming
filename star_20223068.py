n = int(input("n > "))

for i in range(n):
    for k in range(n, i, -1):
        print(" ", end="")

    for k in range((i+1)*2-1):
        print("*", end="")

    print()
