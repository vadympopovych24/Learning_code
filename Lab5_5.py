
number = int(input('Input number: '))

if number > 1:
    i = 2
    while i != int(number ** 0.5) + 1:
        if (number % i) == 0:
            print('This is not a simple number')
            break
        i += 1
    else:
        print('This is a simple number')
else:
    print('This is not a simple number')