import random

lotto_str = ""
cnt = 0

while cnt < 10 :
    num = random.randint(1, 45)

    if num < 10 :
        ran = "0" + str(num)

    else :
        ran = str(num)

    i = 0
    check = True

    while i < cnt :
        if lotto_str[i:i+2] == ran :
            check = False

        i += 2

    if check == True :
        lotto_str += ran
        cnt += 2

cnt = 0

while cnt < 10 :
    print(lotto_str[cnt:cnt+2], end=" ")
    cnt += 2




