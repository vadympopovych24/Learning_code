
h = float(input('Enter h door: '))
w = float(input('Enter w door: '))

a = float(input('Enter a box: '))
b = float(input('Enter b box: '))
c = float(input('Enter c box: '))

if ((a < h and b < w)
    or (a < h and c < w)
    or (b < h and c < w)

    or (a < w and b < h)
    or (a < w and c < h)
    or (b < w and c < h)):
    print('The box enters the door')
else:
    print('The box not come in') 