# 答えたけどオーバーフロー起きそう
import itertools
import random
N = int(input())
A = list(map(int, input().split()))
#N = random.randint(4, 30000)
#A = [random.randint(1, 20) for i in range(N)]

com = list(itertools.combinations(range(N), 2))
ans = len(com)
count = 0
for i in range(N):
    if(A[com[i][0]] == A[com[i][1]]):
        count += 1

print(count)
print(ans-count)
