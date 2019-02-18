# Inspired by this tweet, today's challenge is to calculate the additive persistence of a number, defined as how many
# loops you have to do summing its digits until you get a single digit number. Take an integer N:
#
# Add its digits
#
# Repeat until the result has 1 digit
#
# The total number of iterations is the additive persistence of N.
#
# Your challenge today is to implement a function that calculates the additive persistence of a number.
#
# Examples
# 13 -> 1
# 1234 -> 2
# 9876 -> 2
# 199 -> 3

def sum_digit(number_to_sum):
    result = 0
    while number_to_sum:
        result += number_to_sum % 10
        number_to_sum //= 10
    return result


def additive_persistence(number_to_add_per):
    add_per = 0
    while number_to_add_per // 10 != 0:
        number_to_add_per = sum_digit(number_to_add_per)
        add_per += 1
    return add_per


if __name__ == "__main__":
    print(additive_persistence(13))
    print(additive_persistence(1234))
    print(additive_persistence(9876))
    print(additive_persistence(199))
