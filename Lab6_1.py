def input_sides() -> list:
    print("Enter 3 side triangle: ")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    return [a, b, c]


def area(sides: list) -> float:
    p = (sides[0] + sides[1] + sides[2]) / 2
    area = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
    return area


def output(area: float) -> float:
    print('Area of triangle is %0.3f' % area)


track = area(input_sides())
output(track)

