def only_numberic(string):
    string_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for s in string:
        if s not in string_digit:
            return False
    return True


def isNumeric(string):
    string_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dot_flag = 0
    if string[0] == "-" or string[0] == "+":
        string = string[1:]
    for i in range(len(string)):
        if string[i] in string_digit:
            continue
        if string[i] == "." and dot_flag == 0:
            dot_flag = 1
            return only_numberic(string[i + 1:])
        elif string[i] == "." and dot_flag == 1:
            return False
        if string[i] == "E" or string[i] == "e":
            if i == len(string) - 1:
                return False
            if string[i + 1] == "+" or string[i + 1] == "-":
                return only_numberic(string[i + 2:])
        if string[i] == "+" or string[i] == "-":
            return False
    return True


print(isNumeric("-1e-16"))
