from decimal import Decimal, ROUND_HALF_UP

previous = int(input())
current = int(input())

if current >= previous:
    used = current - previous
else:
    used = 10000 - previous + current

if used <= 300:
    payment = Decimal("21")
elif used <= 600:
    payment = Decimal("21") + (used - 300) * Decimal("0.06")
elif used <= 800:
    payment = Decimal("39") + (used - 600) * Decimal("0.04")
else:
    payment = Decimal("47") + (used - 800) * Decimal("0.025")

if used > 0:
    average = payment / used
    average = average.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
else:
    average = "не определена"

payment = payment.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print("Предыдущее:", previous)
print("Текущее:", current)
print("Использовано:", used)
print(f"К оплате: {payment:.2f}")
print("Ср. цена м^3:", average)
