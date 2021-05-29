N = int(input())
d = [input() for i in range(N)]

# 重複削除してカウント
print(len(set(d)))
