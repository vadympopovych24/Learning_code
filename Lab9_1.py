def gameBlackJack(cards: str) -> int:

    kartu = cards.split()
    card_table = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, "K": 10, 'A': 0}
    amount = sum([card_table[_] for _ in kartu])
    if 'A' in cards:
        ace = 21 - amount
        if ace < 11:
            amount = amount + 1
        elif ace > 11:
            amount = amount + 11
        else:
            amount = amount + ace
    return amount

def output(result: int) -> None:

    if result > 21:
        print("Bust")
    elif result == 21:
        print("BlackJack!!!") 
    else:
        print(result)

output(gameBlackJack(input("Input your cards: ")))