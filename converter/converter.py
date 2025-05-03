import time

while True:
    print("Добро пожаловать в конвертер валют!\n")

    print("1. - USD -> UAH")
    print("2. - UAH -> USD")
    print("3. - EUR -> UAH")
    print("4. - UAH -> EUR\n")

    user_choice = input("Выберите вариант конвертации: ")
    if user_choice not in ["1", "2", "3", "4"]:
        print("Введите корректное значение.")
        time.sleep(1)
        print("Перезапуск программы...")
        time.sleep(1)
        continue

    if user_choice == "1":
        print("Ваш выбор USD -> UAH.\n")
        try:
            x = float(input("Введите сумму: \n"))
        except ValueError:
            print("Введите число.")
            time.sleep(1)
            continue
        summ = x * 41.7
        print(f"Ответ: {summ:.2f}UAH.\n")
        ask = input("Хотите продолжить? Y/N: ")
        if ask.lower() == "y":
            continue
        elif ask.lower() == "n":
            print("Выход из программы...")
            time.sleep(0.5)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            break
    elif user_choice == "2":
        print("Ваш выбор UAH -> USD.\n")
        try:
            x = float(input("Введите сумму: \n"))
        except ValueError:
            print("Введите число.")
            time.sleep(1)
            continue
        summ = x / 41.7
        print(f"Ответ: {summ:.2f}USD.\n")
        ask = input("Хотите продолжить? Y/N: ")
        if ask.lower() == "y":
            continue
        elif ask.lower() == "n":
            print("Выход из программы...")
            time.sleep(0.5)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            break
    elif user_choice == "3":
        print("Ваш выбор EUR -> UAH.\n")
        try:
            x = float(input("Введите сумму: \n"))
        except ValueError:
            print("Введите число.")
            time.sleep(1)
            continue
        summ = x * 47.3
        print(f"Ответ: {summ:.2f}UAH.\n")
        ask = input("Хотите продолжить? Y/N: ")
        if ask.lower() == "y":
            continue
        elif ask.lower() == "n":
            print("Выход из программы...")
            time.sleep(0.5)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            break
    elif user_choice == "4":
        print("Ваш выбор UAH -> EUR.\n")
        try:
            x = float(input("Введите сумму: \n"))
        except ValueError:
            print("Введите число.")
            time.sleep(1)
            continue
        summ = x / 47.3
        print(f"Ответ: {summ:.2f}EUR.\n")
        ask = input("Хотите продолжить? Y/N: ")
        if ask.lower() == "y":
            continue
        elif ask.lower() == "n":
            print("Выход из программы...")
            time.sleep(0.5)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            break
    else:
        print("Введите корректное значение.")
        time.sleep(1)
        continue
