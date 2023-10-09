def solution(blocks):
    n = len(blocks)
    max_distance = 0
    start = 0 
    
    for end in range(1, n):
        if blocks[end] < blocks[end - 1]:
            start = end
        max_distance = max(max_distance, end - start + 1)
    
    return max_distance

print(solution([2, 6, 8, 5]))   
print(solution([1, 5, 5, 2, 6]))
print(solution([1,1]))



    
    