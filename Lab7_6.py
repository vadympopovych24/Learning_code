

def frame_output() -> str:

    text = input('Input your text: ')
    print('*' * len(text) + "****")
    print("*", text, "*")
    print('*' * len(text) + "****")

frame_output()