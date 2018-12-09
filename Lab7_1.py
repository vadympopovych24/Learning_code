

def input_data() -> list:

    your_string = input('Input your string: ')
    shift_number = int(input('Enter number for shift elements of the line: '))

    return [your_string, shift_number]

def shift_elements(string: list) -> str:

    first = string[0][0: string[1]]
    second = string[0][string[1] :]

    new_string = second + first

    return(new_string)

def output_data(new_string: str) -> str:

    print(new_string)

output_data(shift_elements(input_data()))