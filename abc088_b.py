N = int(input())
A = list(map(int, input().split()))

sort = sorted(A, reverse=True)

a = list()
b = list()

# ListにKey,Valをもたせる
for num, val in enumerate(sort):
    if(num%2 == 0):
        a.append(val)
    else:
        b.append(val)


print(sum(a) - sum(b))