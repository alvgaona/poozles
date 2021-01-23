def solution(A):
    number_of_integers = len(A)
    if number_of_integers < 2 or number_of_integers > 100000:
        raise Exception("Number of integers exceeds the limits")
    
    first_part = A[0]
    second_part = 0
    
    for integer in A[1:]:
        second_part += integer
    
    minimal_difference = abs(first_part - second_part)
    
    if number_of_integers > 2:
        for p in range(1, len(A) - 1):
            first_part += A[p]
            second_part -= A[p]
            
            difference = abs(first_part - second_part)
            
            if difference < minimal_difference:
                minimal_difference = difference
    
    return minimal_difference


if __name__ == '__main__':
    A = [-10, -20, -30, -40, 100]
    
    print("Input: {}".format(A))
    print("Minimal difference: {}".format(solution(A)))
