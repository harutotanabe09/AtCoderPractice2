N,A,B = list(map(int, input().split()))

ans = 0

for i in range(N+1):
    # 桁数の合計
    result = sum(list(map(int, str(i))))
    if(result >= A and result <= B):
        ans += i

print(ans)