A, B, C, X = [int(input()) for i in range(4)]

res = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            ans = (500 * i) + (100 * j) + (50 * k)
            if ans == X:
                res += 1

print(res)