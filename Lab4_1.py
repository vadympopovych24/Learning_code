import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))

if (a>=0 and b>0):
    x = math.sqrt(a * b) / (pow(math.e, a)*b) + a*(pow(math.e,2*a/b))
    print ('x = ',x)

else:
    print('a or b is not entered correctly!') 
