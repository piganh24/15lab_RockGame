def sum_numbers_for(n):
    """
    Обчислює суму чисел від 0 до n.

    >>> sum_numbers_for(5)
    15
    >>> sum_numbers_for(0)
    0
    >>> sum_numbers_for(-3)
    0
    >>> sum_numbers_for("abc")
    'Помилка: введене значення не є числом!'
    """
    try:
        n = int(n)
        if n <= 0:
            return 0
        return sum(i for i in range(n + 1))
    except ValueError:
        return "Помилка: введене значення не є числом!"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    try:
        num = int(input("Введіть додатне ціле число: "))
        print(f"Сума чисел від 0 до {num} дорівнює {sum_numbers_for(num)}")
    except ValueError:
        print("Помилка: введене значення не є числом!")
