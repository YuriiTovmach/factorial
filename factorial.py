#factorial with while

# number = int(input("введите число:"))
# i = 1
# factorial = 1
# while i <=number:
#     factorial *= i
#     i +=1
# print("факториал числа", number, "равен", factorial)




# factorial with for

number = int(input("Введите число: "))
factorial = 1
for i in range(1, number+1):
    factorial *= i
print("Факториал числа", number, "равен", factorial)