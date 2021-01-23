#!/bin/python3

def camelcase(s):
    upper_case_letters = set(range(65, 91))
    
    word_count = 1
    
    for letter in s:
        if ord(letter) in upper_case_letters:
            word_count += 1
    
    return word_count


if __name__ == '__main__':
    s = "saveChangesInTheEditor"
    
    assert(camelcase(s) == 5)
