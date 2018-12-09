def input_text() ->str:

    text = input('Input your text: ')
    return(text)

def codding_text(text: str) -> str:
    
    cod_text = list(map(lambda x: chr(ord(x) + 1), text))
    return ''.join(cod_text)

def output_codding_text(cod_text: str) -> str:

    print(cod_text)

output_codding_text(codding_text(input_text()))