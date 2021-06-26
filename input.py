import random
N = random.randint(4, 30000)
A = [random.randint(1, 20) for i in range(N)]
print(N)
print(*A)