# https://atcoder.jp/contests/abc203/tasks/abc203_c
n, k = map(int,input().split())
mp = [list(map(int,input().split())) for i in range(n)]
mp.sort(key=lambda x: x[0])
 
sum = k
for i in range(n):
    if mp[i][0] <= sum:
        sum += mp[i][1]
 
print(sum)