import math
n = 0

for x in range(1, 101) :
    n += (1/x)
print(n)


k = (math.log(101))
print(k)

print(f"{((k -  n) / n)}")