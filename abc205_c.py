A,B,C = map(int, input().split())

# 奇数かどうか
if C % 2 !=0 :
    if (A > B):
        print(">")
    elif (A < B):
        print("<")
    else:
        print("=")
else:
    if (abs(A) > abs(B)):
        print(">")
    elif (abs(A) < abs(B)):
        print("<")
    else:
        print("=")