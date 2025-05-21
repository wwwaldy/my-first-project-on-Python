import random
import time

print("🪙 Орел или Решка?\n")

def flip_coin():
    base = ["орел", "решка"]
    user_choice = input("🤔 Выбери, Орел или Решка?: ").lower()
    while user_choice not in base:
        print("🚫 Введите корректное значение!\n")
        time.sleep(1)
        user_choice = input("Выберите еще раз, Орел или Решка?: ").lower()
    pc_choice = random.choice(base)
    print("Ты выбрал:", user_choice.capitalize())
    time.sleep(1)
    print("\n🪙 Монета подбрасывается...")
    time.sleep(1)
    print("🪙 Монета крутится...")
    time.sleep(1)
    print("🪙 Монета падает...")
    time.sleep(1)
    print("\n👌🏻 Монета упала на:", pc_choice.capitalize())
    time.sleep(0.5)
    if user_choice == pc_choice:
        print("🎉 Ты выиграл!")
        time.sleep(1)
    else:
        print("😭 Ты проиграл!")
        time.sleep(1)

def main():
    while True:
        flip_coin()
        play_again_base = ["да", "нет"]
        play_again = input("\n🤔 Хотите сыграть еще раз? Да/Нет: \n")
        while play_again.lower() not in play_again_base:
            print("🚫 Введите корректное значение!\n")
            time.sleep(1)
            play_again = input("\n🤔 Хотите сыграть еще раз? Да/Нет: \n")
        if play_again.lower() != "да":
            time.sleep(0.5)
            print("Выход из игры...")
            time.sleep(0.5)
            print(3)
            time.sleep(0.5)
            print(2)
            time.sleep(0.5)
            print('1...')
            time.sleep(0.5)
            print("👌🏻 Спасибо за игру!")
            break
        else:
            time.sleep(1)
            print("🪙 Начинаем новую игру...\n")
            time.sleep(1)
    
if __name__ == "__main__":
    main()

