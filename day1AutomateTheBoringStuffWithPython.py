def collatz(number):
    result = None
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif  number % 2 == 1:
        result = 3*number+1
        print(result)
        return result
    else:
        return result

a=None
print('Please enter a integer')
a=int(input())
while a != 1:
    a = collatz(a)
