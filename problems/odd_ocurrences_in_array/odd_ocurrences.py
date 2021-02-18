# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array

def odd_ocurrences(array):
    not_repeated = set()
    repeated = set()
    
    for num in array:
        if num in not_repeated:
            not_repeated.remove(num)
            repeated.add(num)
        else:
            not_repeated.add(num)
    
    return [num for num in not_repeated][0]
