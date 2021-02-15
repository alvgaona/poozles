# https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(text):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    upper_case_letters = set(range(65, 91))
    
    word_count = 1
    
    for letter in text:
        if ord(letter) in upper_case_letters:
            word_count += 1
    
    return word_count
