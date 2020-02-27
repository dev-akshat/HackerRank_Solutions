def print_formatted1(number):
    w = len(str(bin(number)).replace('0b', ''))
    for x in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(x, width=w))


def print_formatted2(number):
    w = len(str(bin(number)).replace('0b', ''))
    for i in range(1, number + 1):
        d = str(i).rjust(w, ' ')
        b = bin(i)[2:].rjust(w, ' ')  ## rjust is used for line alignment
        o = oct(i)[2:].rjust(w, ' ')
        h = hex(i)[2:].rjust(w, ' ').upper()
        print(d, o, h, b)


def print_formatted3(number):
    w = len(str(bin(number)).replace('0b', ''))
    for x in range(1, number + 1):
        print(
            str(x).rjust(w, " "),
            format(x, 'o').rjust(w, " "),
            format(x, 'x').rjust(w, " "),
            format(x, 'b').rjust(w, " ")
        )


n = 3
print_formatted1(n)
print()
print_formatted1(n)
print()
print_formatted3(n)
