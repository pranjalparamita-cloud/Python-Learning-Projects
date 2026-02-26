print("-----------Lets check the strength of your password!-----------")
password = input("Enter your password: ")
strength = 0
while True:
    if not password:
        print("Password cannot be empty.")
    else:
        if len(password) < 4:
            print("Password is too short.")
        elif len(password) > 9:
            print("Password is too long.")
        else:
            print("Password length is good.")
            strength += 1
        if any(char.islower() for char in password):
            strength += 1
        if any(char.isdigit() for char in password):
            strength += 1
        if any(char.isupper() for char in password):
            strength += 1
        if any(char in "!@#$%^&*()-+" for char in password):
            strength += 1
        if strength == 5:
            print("Password is strong. You are allowed to proceed.")
        elif strength >= 3:
            print("Password is medium. You may proceed with caution.")
        else:
            print("Password is weak. Please choose a stronger password.")
            print("Try again!")
            password = input("Enter your password: ")
            continue
    break