def delete_whitespaces(text: str) -> str:

    return ' '.join(text.split())

print(delete_whitespaces(input("Input your text: ")))