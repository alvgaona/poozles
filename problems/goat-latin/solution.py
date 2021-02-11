#!/usr/bin/python3

def to_goat_latin(text: str) -> str:
    words = text.split(" ")
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    output = []
    for index, word in enumerate(words):
        if word[0] not in vowels:
            word = word[1:] + word[:1]
        word = word + 'ma' + 'a' * (index + 1)
        output.append(word)

    return ' '.join(output)


if __name__ == '__main__':
    text = 'The quick brown fox jumped over the lazy dog'

    assert to_goat_latin(text) == 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa ' + \
           'azylmaaaaaaaaa ogdmaaaaaaaaaa'