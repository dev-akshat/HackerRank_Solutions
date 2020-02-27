def rotLeft(a, d):
    for x in range(d):
        temp = a[0]
        a.pop(0)
        a.append(temp)
    return a


no_of_inputs = 5
no_of_rotation = 4
my_str = "1 2 3 4 5"
my_arr = [s for s in my_str.strip().split()]
print(rotLeft(my_arr, no_of_rotation))
