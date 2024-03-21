def solution(n):
    
    def hanoi(n, fir, mid, end):
        if n == 1:
            answer.append([fir,end])
            return
        
        hanoi(n-1,fir,end,mid)
        answer.append([fir,end])
        hanoi(n-1,mid,fir,end)
            
    answer = []
    hanoi(n,1,2,3)
    return answer