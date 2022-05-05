allSet = [{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {1, 3, 5, 7, 12, 15}, {3, 12, 15, 18, 20}, {12, 13, 14, 15, 16, 17, 18, 19}]

cnt = 3
for i in range(len(allSet)):
    for j in range(cnt):
        J = len(allSet[i] & allSet[i+j+1]) / len(allSet[i] | allSet[i+j+1])
        print(J)
    print('-'*60)
    cnt -= 1
