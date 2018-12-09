import decimal
import math

def input_data() -> list:

    money = decimal.Decimal(input("Input amount of money: "))
    required_money = decimal.Decimal(input("Input required amount of money: "))
    procent = decimal.Decimal(input("Input interest rate of the bank: "))

    return [money, procent, required_money]

def output_result(result: str) -> None:


    result = str(result)
    print("Duration of deposit: ", result)


def calculate_deposit_year(deposit: list) -> float:


    duration = math.log(deposit[2] / deposit[0], (1 + deposit[1] / 100))

    return duration

output_result(calculate_deposit_year(input_data()))