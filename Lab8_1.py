
def last_number_person(num: int) -> int:
    n = list(range(1, num + 1))
    count = 0
    while len(n) > 1:
        first = n.pop(0)
        if count % 3:
            n.append(first)
            count = 0
        else:
            count += 1
    return n

print(last_number_person(10))