import random
import time
Ввод количества примеров
while True:
try:
n = int(input("Введите количество примеров: "))
if n > 0:
break
print("Количество должно быть больше нуля!")
except ValueError:
print("Пожалуйста, введите целое число!")
correct = 0
total_time = 0
for i in range(1, n + 1):
a = random.randint(2, 9)
b = random.randint(2, 9)
print(f"\nВопрос {i}/{n}")
start_time = time.perf_counter()

# При неправильном формате ввода повторяем тот же пример
while True:
    try:
        answer = int(input(f"{a} × {b} = "))
        break
    except ValueError:
        print("Пожалуйста, введите целое число!")

elapsed = time.perf_counter() - start_time
total_time += elapsed

if answer == a * b:
    correct += 1
    print(f"Верно! (Время: {elapsed:.1f} сек)")
else:
    print(
        f"Неверно! Правильно: {a * b} "
        f"(Время: {elapsed:.1f} сек)"
    )
print("\n" + "=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time / n:.1f} сек")
print(f"Правильных ответов: {correct}/{n}")
print(f"Процент правильных: {correct / n * 100:.1f}%")
