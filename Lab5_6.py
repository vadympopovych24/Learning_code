side_A = float(input('A side of triangle: '))
side_B = float(input('B side of triangle: '))
side_C = float(input('C side of triangle: '))

hypotenuse = max(side_A, side_B , side_C)
sides_sum = (side_A + side_B  + side_C) - hypotenuse

if ((side_A <= 0)
        or (side_B <= 0)
        or (side_C <= 0)):
    print("Triangle does not exist")
elif sides_sum > hypotenuse:
    print("Triangle exists")
else:
    print("Triangle does not exist")