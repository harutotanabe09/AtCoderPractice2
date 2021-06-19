N, Y = map(int, input().split())

resA = -1
resB = -1
resC = -1

for a in range(N+1):
    for b in range(N+1-a):
        c = N - a - b
        total = 10000*a + 5000*b + 1000*c
        if(Y == total):
            resA = a
            resB = b
            resC = c
            break

print('%d %d %d' % (resA, resB, resC))