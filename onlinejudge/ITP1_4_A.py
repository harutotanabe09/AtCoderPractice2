# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_A

a, b = map(int, input().split())
print('%d %d %f' % (a // b, a % b, float(a/b)))