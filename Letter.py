


def letter(words):

    a = ''
    for word in words:
        a+=word

    letter = {letters for letters in a}
    return sorted(list(letter))



def letter(words):

    a = ''.join(words)
    print(a)
    letter = {letters for letters in a}
    return sorted(list(letter))




print(letter(['xww','wxyz','ywx','ywz']))
