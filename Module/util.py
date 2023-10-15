def find_max(number):
    max = number[0]

    for x in number:
        if max < x:
            max = x
    return max