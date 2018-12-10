import functools

def middle(source: list) -> float:

    return functools.reduce((lambda x, y: x + y), source) / len(source)

print(middle([2, 4, 6, 9, 9, 2, 1, 1]))

def median(lst: list) -> float:

    number = len(lst)
    if len(lst) % 2 == 1:
        return sorted(lst)[number//2]
    else:
        return sum(sorted(lst)[number//2-1:number//2+1])/2

print(median([2, 4, 6, 9, 9, 2, 1, 1]))