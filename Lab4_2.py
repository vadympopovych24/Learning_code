
import math

print('Enter 3 real numbers')
a = float(input('Input number a: '))
b = float(input('Input number b: '))
c = float(input('Input number c: '))
f = 1/(c*math.sqrt(2*math.pi))*math.exp(-((a-b)**2)/(2*c**2))
print('f =',f)
