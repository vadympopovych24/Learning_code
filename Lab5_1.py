

number = int(input('Input positive number: '))
print("Is there a number" ,number, "degree of two?")
if  (number != 0 and ((number & (number - 1)) == 0)):
    print("Number"  , number , " is a degree of two ")
else:
    print("Number"  , number , " is not degree of two" ) 