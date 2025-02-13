def sum_numbers_for(n):
    try:
        n = int(n)
        if n <= 0:
            return 0
        return sum(i for i in range(n + 1))
    except ValueError:
        return "Помилка: введене значення не є числом!"

try:
    num = int(input("Введіть додатне ціле число: "))
    print(f"Сума чисел від 0 до {num} дорівнює {sum_numbers_for(num)}")
except ValueError:
    print("Помилка: введене значення не є числом!")
