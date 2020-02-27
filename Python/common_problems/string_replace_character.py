def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


def mutate_string2(string, position, character):
    li = list(string)
    li[position] = character
    return "".join(li)


print(mutate_string("abcde", 2, "z"), mutate_string2("abcde", 2, "z"))
print("aBcDe".swapcase())
