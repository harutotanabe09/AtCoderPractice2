N = int(input())

# point // で割る
h = N // 3600
m = (N % 3600) // 60
s = ((N % 3600) % 60)

print('%d:%d:%d' % (h, m,s))