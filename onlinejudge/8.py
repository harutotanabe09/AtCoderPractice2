# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_D
W , H , x , y , r = list(map(int, input().split()))

x1 = x + r
x2 = x - r
y1 = y + r
y2 = y - r

if (W >= x1 and 0 <= x2 and H >= y1 and 0 <= y2 ):
    print("Yes")
else:
    print("No")