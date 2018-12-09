import decimal

def input_data() -> list:

    money = decimal.Decimal(input("Input amount available of money: "))
    procent = decimal.Decimal(input("Input interest rate of the bank in %: "))
    duration = decimal.Decimal(input("Input duration in years: "))

    return [money, procent, duration]

def output_result(result: str) -> None:

    result = str(result)
    print("Amount at the moment of deposit agreement completion.: ", result)

def summary_money(deposit: list) -> float:

    if len(deposit) != 3:
        print("Too many or less members of list")
        exit()

    sum_deposit = deposit[0] * (1 + deposit[1] / 100) ** deposit[2]

    return sum_deposit




output_result(summary_money(input_data()))