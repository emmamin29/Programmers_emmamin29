def solution(arr, k):
    if k % 2 == 1:
        answer = [num * k for num in arr]
    else:
        answer = [num + k for num in arr]
            
    return answer