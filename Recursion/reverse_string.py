old_str = str(input("Enter the string "))
new_str = ''
# print(old_str[len(old_str) - 1])

# print(len(new_str))


def rev_str(old_str, new_str):
    if len(old_str) <= 0:
        return new_str
    new_str = new_str + old_str[len(old_str) - 1]
    old_str = old_str[0:len(old_str) - 1]
    # print(old_str)
    return rev_str(old_str, new_str)


print(rev_str(old_str, new_str))
