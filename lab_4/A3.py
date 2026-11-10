Проверяем длину строки и допустимые символы
while True:
packets = input("Введите последовательность из 0 и 1: ")
if len(packets) < 5:
    print("Строка должна содержать не менее 5 символов!")
elif not all(char in "01" for char in packets):
    print("Используйте только символы 0 и 1!")
else:
    break
total = len(packets)
lost = packets.count("0")
Ищем самую длинную последовательность нулей
current = 0
longest = 0
for packet in packets:
if packet == "0":
current += 1
if current > longest:
longest = current
else:
current = 0
loss_percent = lost / total * 100
Граничное значение относим к лучшей категории
if loss_percent <= 1:
quality = "отличное качество"
elif loss_percent <= 5:
quality = "хорошее качество"
elif loss_percent <= 10:
quality = "удовлетворительное качество"
elif loss_percent <= 20:
quality = "плохое качество"
else:
quality = "критическое состояние сети"
print(f"\nОбщее количество пакетов: {total}")
print(f"Количество потерянных пакетов: {lost}")
print(
"Длина самой длинной последовательности "
f"потерянных пакетов: {longest}"
)
print(f"Процент потерь: {loss_percent:.1f}%")
print(f"Качество связи: {quality}")
