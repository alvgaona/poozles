#

# Constraints
length_range = set(range(1, 101))
numbers = set('0123456789')
lower_case = set('abcdefghijklmnopqrstuvwxyz')
upper_case = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
special_characters = set('!@#$%^&*()-+')


def strong_password(n, password):
    # Converting a list to a set has a time complexity of O(n) The password_set at has m values with m <= n. The
    # equality holds if there are no repeated characters. If that's not the case m < n; however, m is upper bounded
    # by the valid characters. So the space complexity does not increase indefinitely.
    password_set = set(password)
    
    if n not in length_range:
        raise Exception("Password length is not admissible")
    
    characters_to_add = 0
    
    has_number = False
    has_lower_case = False
    has_upper_case = False
    has_special_character = False
    
    # This will iterate through the password_set m times.
    # The lookup in the sets is O(1) so it doesn't impact the time complexity
    for password_char in password_set:
        if has_number is False and password_char in numbers:
            has_number = True
        elif has_lower_case is False and password_char in lower_case:
            has_lower_case = True
        elif has_upper_case is False and password_char in upper_case:
            has_upper_case = True
        elif has_special_character is False and password_char in special_characters:
            has_special_character = True
        
        if has_special_character is True and has_upper_case is True and has_lower_case is True and has_number is True:
            break
    
    if has_number is False:
        characters_to_add += 1
    
    if has_special_character is False:
        characters_to_add += 1
        
    if has_lower_case is False:
        characters_to_add += 1
    
    if has_upper_case is False:
        characters_to_add += 1
        
    if 6 - (n + characters_to_add) > 0:
        characters_to_add += 6 - (n + characters_to_add)
        
    return characters_to_add
