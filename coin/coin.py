import random
import time

print("Орел или Решка?\n")

def flip_coin():
    base = ["орел", "решка"]
    user_choice = input("Выбери, Орел или Решка?: ")
    pc_choice = random.choice(base)
    print("Ты выбрал:", user_choice.capitalize())
    time.sleep(1)
    print("\nМонета подбрасывается...")
    time.sleep(1)
    print("Монета крутится...")
    time.sleep(1)
    print("Монета падает...")
    time.sleep(1)
    print("\nМонета упала на:", pc_choice.capitalize())
    if user_choice == pc_choice:
        print("\nТы выиграл!")
    else:
        print("\nТы проиграл!")

def main():
    while True:
        flip_coin()
        play_again = input("\nХотите сыграть еще раз? Да/Нет: \n")
        if play_again != "да":
            time.sleep(0.5)
            print("Выход из игры...")
            time.sleep(0.5)
            print(3)
            time.sleep(0.5)
            print(2)
            time.sleep(0.5)
            print('1...')
            time.sleep(0.5)
            print("Спасибо за игру!")
            break
    
if __name__ == "__main__":
    main()

