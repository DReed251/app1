build = True
while build:
    password = input("Enter new password: ")

    result = {}

    if len(password) >= 8:
        result["lenght"] = True
    else:
        result["lenght"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    upper = False
    for i in password:
        if i.isupper():
            upper = True

    result["upper"] = upper
    print(result)

    if all(result.values()):
        print("Strong Password")
        build = False
    else:
        print("Weak Password")