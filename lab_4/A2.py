def read_positive(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Введите число больше нуля!")
        except ValueError:
            print("Введите целое число!")


def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end="")
        print()


def draw_triangle(rows, ch):
    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end="")
        print()


def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()


n = read_positive("Введите количество строк n: ")
m = read_positive("Введите количество столбцов m: ")

print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
draw_rectangle(n, m, "#")

print("\nПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК:")
draw_triangle(n, "#")

print(f"\nРАМКА {n}x{m}:")
draw_frame(n, m, "#")
