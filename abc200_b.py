N,K = list(map(int, input().split()))

ans = N
for i in range(K):
    if( ans % 200 == 0):
        # TODO: .0 がつかないよに除算
        ans //= 200
    else:
        ans = ans*1000 + 200

print(ans)