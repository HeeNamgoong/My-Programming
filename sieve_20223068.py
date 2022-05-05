import math
n = 50
num = [i for i in range(2, int(math.sqrt(n))+1)]
prime1 = []

for i in num:
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        prime1.append(i)

a = [0] * n

for i in prime1:
    j = i
    while True:
        j += i
        if j >= n:
            break
        a[j] = 1
for i in range(2, n):
    if a[i] == 0:
        print(i, end=" ")

# 첫 번째 방법이 문제의 의도와 제일 부합하는 것 같습니다.
"""
import math
n = 50
num = [i for i in range(2, n+1)]
prime = []

for i in num:
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        prime.append(i)

print(prime)
"""

"""
import math
n = 50

num = [i for i in range(n+1)]
prime = num[:]

for i in range(2,int(math.sqrt(n)+1)):
    j = 2
    while i*j <= n:
        if num[i*j] in prime:
            prime.remove(num[i*j])
        j += 1
print(prime[2:])
"""

