'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, char = 'th'):
    l1 = len(word)
    l2 = len(char)
    if l1 == 0 or l1 < l2:
        return 0
    if word[0 : l2] == char:
        return count_th(word[l2 - 1:], char) + 1
    return count_th(word[l2 - 1:], char)
