import math
N = int(input())
ans = math.floor(N * 1.08)

if(ans>206):
    print(":(")
if(ans==206):
    print("so-so")
if(ans<206):
    print("Yay!")
