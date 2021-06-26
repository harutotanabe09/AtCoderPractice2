# TODO: Counterで連続する要素をグループ化
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
l = list()

for j in range(N):
    l.append(B[C[j]-1])

Count_D=Counter(l)

for i in range(N):
    # 重複しているのがグループ化しているので、その数分を重複カウントされる
    ans = ans + Count_D[A[i]]

print(ans)
