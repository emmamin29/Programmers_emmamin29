import math 
def solution(a, b, c):
    answer = 0
    if a==b and b==c:
        answer = (a+b+c) *(math.pow(a,2)+math.pow(b,2)+math.pow(c,2)) *(math.pow(a,3)+math.pow(b,3)+math.pow(c,3))
    elif (a==b and b!=c )or(a==c and b!=c) or (b==c and a!=b):
        answer = (a+b+c) *(math.pow(a,2)+math.pow(b,2)+math.pow(c,2))
    else:
        answer = a+b+c
    
    return answer