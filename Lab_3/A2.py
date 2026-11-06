import string

password = input()

special = "*-#"
allowed = string.ascii_letters + string.digits + special

reliable = True

if len(password) != 8:
    print("Длина пароля не равна 8")
    reliable = False

if not any(symbol in string.ascii_uppercase for symbol in password):
    print("В пароле отсутствуют заглавные буквы")
    reliable = False

if not any(symbol in string.ascii_lowercase for symbol in password):
    print("В пароле отсутствуют строчные буквы")
    reliable = False

if not any(symbol in string.digits for symbol in password):
    print("В пароле отсутствуют цифры")
    reliable = False

if not any(symbol in special for symbol in password):
    print("В пароле отсутствуют специальные символы")
    reliable = False

if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")
    reliable = False

if reliable:
    print("Надежный пароль")
