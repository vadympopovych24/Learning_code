

def reverse_str() -> bool:

    a = str(input('Enter sentence: '))
    a = a.lower().replace(' ', '')
    a = a.lower().replace('\'', '')

    b = a[::-1]

    c = a == b
    print(c)
    return(c)

reverse_str()