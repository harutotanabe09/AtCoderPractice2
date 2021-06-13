# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/3/ITP1_3_D

a,b,c = list(map(int, input().split()))

ans = 0

for i in range(a,b+1):
    if(c % i == 0):
        ans += 1

print(ans)
