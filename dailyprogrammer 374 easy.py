# Description
# A number is input in computer then a new no should get printed by adding one to each of its digit. If you encounter a
# 9, insert a 10 (don't carry over, just shift things around).
#
# For example, 998 becomes 10109.
#
# Bonus
# This challenge is trivial to do if you map it to a string to iterate over the input, operate, and then cast it back.
# Instead, try doing it without casting it as a string at any point, keep it numeric (int, float if you need it) only.

def add_one_to_each_digit(number):
    res = i = 0
    while number:
        number, digit_seeked = divmod(number, 10)
        res += (digit_seeked + 1) * 10 ** i
        i += 1 + (digit_seeked == 9)
    return res


print(add_one_to_each_digit(998))
