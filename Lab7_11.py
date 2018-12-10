def length_sort(text: str) -> str:

    return ' '.join(sorted(text.split(), key=len)) 

print(length_sort(input("Input your text: ")))