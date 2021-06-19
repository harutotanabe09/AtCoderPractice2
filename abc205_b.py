N = int(input())
A = list(map(int, input().split()))

b = sorted(A)

for i in range(0,N):
    if(i+1 != b[i]):
        print("No")
        exit()

print("Yes")