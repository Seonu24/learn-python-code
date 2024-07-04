def solution(number, n, m):

    if number%(n*m) == 0 :
        return 1

    else :
        return 0
    
print(solution(55, 10, 5))