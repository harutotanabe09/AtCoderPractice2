s = input()

ans = ''
w = ''
# TODO: 文字列を反転する
for i in reversed(s):
    if(i == '6'):
        w = '9'
    elif(i == '9'):
        w = '6'
    else:
        w = i
    ans += w

print(ans)