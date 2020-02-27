def count_substring(string, sub_string):
    if sub_string not in string:
        return 0
    li = [i for i in range(len(string)) if string.startswith(sub_string, i)]
    return len(li)


def count_substring2(string, sub_string):
    count = 0
    start = 0
    while start < len(string):
        flag = string.find(sub_string, start)
        if flag != -1:
            start = flag + 1
            count += 1
        else:
            return count


print(count_substring("ABCDCDC", "CDC"))
print(count_substring2("ABCDCDC", "CDC"))
print("ABCDCDC".count("CDC"))  # no overlapp count
