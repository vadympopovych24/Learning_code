
def find_loud_letters() -> str:

    text = input('Input your text : ')

    loud_letters = text.count('a') + text.count('o') + text.count('u') +\
    text.count('i') + text.count('e') + text.count("y") +\
    text.count('A') + text.count('O') + text.count('U') +\
    text.count('I') + text.count('E') + text.count('Y') +\
    text.count('а') + text.count('е') + text.count("у") +\
    text.count('і') + text.count('и') + text.count('о') +\
    text.count('А') + text.count('Е') + text.count('У') +\
    text.count('І') + text.count('О')
    print(loud_letters)
    return(loud_letters)
find_loud_letters()