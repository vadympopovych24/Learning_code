def create_second_line(first_line, second_line: str) -> bool:

    return not[0 for _ in first_line if first_line.count(_) >second_line.count(_)] 

print(create_second_line(input('Input your first_line: '), input('Input your second_line: ')))