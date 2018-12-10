
import re

def camel_case(text: str) -> str:

    words = text.split('_')
    camel_name = words[0]
    camel_name += ''.join(list(map(str.capitalize, words[1:])))

    return camel_name

def snake_case(text: str) -> str:

    words = re.sub(r'([A-Z])', r" \1", text).split()
    snakeName = '_'.join(list(map(str.lower, words)))

    return snakeName

print(camel_case(input("Input your text in camel_case.Transformed in snakeСase: ")))
print(snake_case(input("Input your text in SnakeCase. Transformed in camel_case: ")))