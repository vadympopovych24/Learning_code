def check_lucky_ticket(number: str) -> bool:

    half_number = int(len(number) / 2)
    first_half = list(map(int, number[0 : half_number]))
    second_half = list(map(int, number[-half_number :]))

    return sum(first_half) == sum(second_half)
print(check_lucky_ticket(input("Input number ticket: ")))