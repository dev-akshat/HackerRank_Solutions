# THE MINION GAME

def minion_game1(string):
    vowels = frozenset("AEIOU")
    kevsc = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevsc += length - i
    result = 2 * kevsc - (length * (length + 1) // 2)
    if result > 0:
        print("Kevin", kevsc)
    elif result < 0:
        print("Stuart", kevsc - result)
    else:
        print("Draw")


def minion_game2(string):
    vowels = frozenset("AEIOU")
    length = len(string)
    kevsc = sum(((length - i) for i in range(length) if string[i] in vowels))
    result = 2 * kevsc - (length * (length + 1) // 2)
    if result > 0:
        print("Kevin", kevsc)
    elif result < 0:
        print("Stuart", kevsc - result)
    else:
        print("Draw")


st = "BANANA"
minion_game1(st)
minion_game2(st)
