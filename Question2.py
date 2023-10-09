def solution(S):
    letter_count = {}

    for letter in S:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    deletions_needed = 0
    
    for count in letter_count.values(): 
        if count % 2 != 0:
            deletions_needed += 1
    return deletions_needed 

print(solution("acbcbba"))  # Should return 1
print(solution("axxaxa"))   # Should return 2
print(solution("aaaa"))     # Should return 0

#############################################################################################################


S= "We Test Coders"

def reverse_words(S):
    words=S.split()

    reversed_words= [word[::-1] for word in words]
    return (" ".join(reversed_words))



print(reverse_words(S))