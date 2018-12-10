def valid_email(email: str) -> bool:

    em = email.split('@')[1].split('.')
    return len(em[-1]) > 1 and email.count('@') < 2 and len(em) > 1

print(valid_email(input("Input your email: ")))