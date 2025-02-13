def sum_numbers_while(n):
    if n <= 0:
        return 0
    return sum(i for i in range(n + 1))

num = int(input("Введіть додатнє число: "))
print("Сума від 0 до ",num ," = ", sum_numbers_while(num))