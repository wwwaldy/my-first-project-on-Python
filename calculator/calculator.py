import time as t

print("Я твой быстрый калькулятор!\n")


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_user_input():
    operation = input("Введите операцию (+, -, *, /): \n")
    if operation not in ['+', '-', '*', '/']:
        print("\nНеверная операция. Попробуйте снова.")
        return get_user_input()
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("\nНеверный ввод. Пожалуйста, введите числа.")
        return get_user_input()
    return operation, num1, num2


def main():
    while True:
        operation, num1, num2 = get_user_input()

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = substract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            if num2 == 0:
                print("\nНа ноль делить нельзя!")
                continue  # ← Переход к следующей итерации, не продолжаем выполнение
            result = divide(num1, num2)

        print(f"\nРезультат: {result}")
        again = input("Хотите продолжить? (да/нет): ").strip().lower()
        if again != 'да':
            print("Спасибо за использование калькулятора!")
            break

        t.sleep(1)
        print("Перезапускаю калькулятор...")
        t.sleep(1)
        print("Калькулятор перезапущен!")
        t.sleep(1)


main()
