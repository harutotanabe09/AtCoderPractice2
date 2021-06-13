N,K = list(map(int, input().split()))

rNo = 0
ans = 0
for i in range(1,N+1):
    for j in range(1,K+1):
        rNo = i * 100 + j
        ans = ans + rNo

print(ans)