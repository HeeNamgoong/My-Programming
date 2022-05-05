import time
import random
low = 1
high = 1000
iter = 1000
a = []

for i in range(iter):
    a.append(random.randint(low, high))

start1 = time.time()
a.sort()
end1 = time.time()


print("Running sort(%d) takes %s" %(iter, end1-start1))
start2 = time.time()
for j in range(len(a)):
    for i in range(0, len(a)-1):
        if a[i] >= a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
end2 = time.time()

print("Running bubble(%d) takes %s" %(iter, end2-start2))
print(a)