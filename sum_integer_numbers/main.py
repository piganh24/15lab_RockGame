def sum_numbers_while(n):
    if n <= 0:
        return 0
    
    total = 0
    i = 0
    while i <= n:
        total += i
        i += 1

    return total

num = int(input("Введіть додатнє число: "))
print("Сума від 0 до ",num ," = ", sum_numbers_while(num))