# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_C
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/2/ITP1_2_C
a,b,c = list(map(int, input().split()))

list = [a,b,c]
list = sorted(list)

print('%d %d %d' % (list[0], list[1],list[2]))