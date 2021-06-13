N = int(input())
list = []

max=0

# inputが以下のケース
# N
# S1 T1
# SN TS
for i in range(N):
    a,b=input().split()
    list.append([a, int(b)])

# TODO: 2次元配列のソート方法
li = sorted(list, reverse=True, key=lambda x: x[1])
# 2番目に大きい
print(li[1][0])