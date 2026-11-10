def is_valid_card(number):
# Допускаем только обычные цифры
if not all("0" <= char <= "9" for char in number):
return False

if not 13 <= len(number) <= 19:
    return False

# Отбрасываем номера из одинаковых цифр
if len(set(number)) == 1:
    return False

total = 0

# Перебираем цифры справа налево
for i, char in enumerate(reversed(number)):
    digit = int(char)

    # Удваиваем каждую вторую цифру
    if i % 2 == 1:
        digit *= 2

        if digit > 9:
            digit -= 9

    total += digit

return total % 10 == 0card_number = input(
"Введите номер карты без пробелов и дефисов: "
)

if is_valid_card(card_number):
print("Номер карты прошёл проверку.")
else:
print("Номер карты некорректен.")
