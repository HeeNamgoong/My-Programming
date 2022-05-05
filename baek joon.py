"""

A, B = map(int, input().split())

if A > B:
    print(">")
if A < B:
    print("<")
if A == B:
    print("==")
"""
"""
score = int(input())

if 90 <= score <= 100 :
    print("A")
elif 80 <= score <= 89 :
    print("B")
elif 70 <= score <= 79 :
    print("C")
elif 60 <= score <= 69 :
    print("D")
else :
    print("F")
"""
""""
year = int(input())

if year % 4 == 0 and (not year % 100 ==0 or year % 400 == 0) :
    print(1)
else :
    print(0)
"""

"""
x = int(input())
y = int(input())

if x < 0 and y < 0 :
    print(3)
elif x<0 and y>0 :
    print(2)
elif x>0 and y<0 :
    print(4)
elif x>0 and y>0 :
    print(1)
"""
"""
H, M = map(int, input().split())

CY = (H*60 + M) - 45

H_ = CY // 60
M_ = CY % 60

if H_ < 0:
    H_ = 23

print(H_, M_)
"""

"""
# 오븐 시계
A, B = map(int, input().split())
C = int(input())

total_ = (A * 60) + B + C 

H = total_ // 60
M = total_ % 60

if A > 12 :
    A = A - 12

if H > 23 :
    H = H - 24

print(H, M)
"""


"""
A, B, C = map(int, input().split())
ls_ = [A, B, C]

if A == B == C :
    print(10000+(A*1000))
elif A == B and B != C:
    print(1000+(B*100))
elif A == C and B != C:
    print(1000+(A*100))
elif C == B and B != A:
    print(1000+(B*100))
elif A != B != C:
    print(max(ls_)*100)
"""

"""
n = int(input())

i = 1

for i in range(n):
    i += 1
    print(i)
"""
"""
n = int(input())

for i in range(n, 0, -1):
    print(i)
"""

"""
T = int(input())

for x in range(1, T+1):
    A, B = map(int,input().split())
    print(f"Case #{x}: {A} + {B} = {A + B}")    
"""
"""
import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
"""

"""
#X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
"""

"""
while True:
    A, B = map(int, input().split())
    if A and B == 0:
        break
    else:
        print(A+B)
"""
"""
#26 2+6 = 8, 6+8=14, 8+4=12, 4+2=6, 26
N = int(input())

a = N // 10
b = N % 10

result = N-1
cnt = 0

while N != result:
    c = a + b
    result = b * 10 + c % 10
    a = b
    b = c % 10
    cnt += 1
print(cnt)
"""

"""
N = int(input())
a = list(map(int, input().split()))
print(min(a), end=" ")
print(max(a))
"""
"""
ls = []

for i in range(9):
    ls.append(int(input()))

print(max(ls))
print(ls.index(max(ls))+1)
"""
"""
A, B, C = map(int, input().split())
sup = list(str(A*B*C))
print(sup)

for i in range(10):
    print(sup.count(str(i)))
"""
"""
A, B, C = map(int, input().split())
sup = list(str(A*B*C))
cnt = 0
for i in range(10):
    cnt += 1
    print(cnt)
"""
A = []
B = []
for i in range(10):
    b = int(input())
    A.append(b)
for j in A:
    a = j % 42
    print(a)
if a not in A:
    B.append(a)
print(len(B))
