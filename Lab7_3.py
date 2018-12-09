
def rejecting_brackets() -> bool:

    expression = input("Input your string: ")
    open_brackets = tuple('([{<')
    close_brackets = tuple(')]}>')
    reflection = dict(zip(open_brackets, close_brackets))
    queue = []

    for letter in expression:
        if letter in open_brackets:
            queue.append(reflection[letter])
        elif letter in close_brackets:
            if not queue or letter!= queue.pop():
                print(False)

    print(not queue)

    return queue
rejecting_brackets()