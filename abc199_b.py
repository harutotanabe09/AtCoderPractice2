# https://atcoder.jp/contests/abc199/editorial/1161
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
x = max(a)
y = min(b)
z = []
 
for i in range(x, y+1):
    z.append(i)
 
print(len(z))