def sum_numbers_while(n):
    if n <= 0:
        return 0
    
    total = 0
    i = 0
    for i in range(n + 1):
        total += i
        

    return total

num = int(input("Введіть додатнє число: "))
print("Сума від 0 до ",num ," = ", sum_numbers_while(num))