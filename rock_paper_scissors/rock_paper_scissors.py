import time as t
import random

print('Игра "Камень, ножницы, бумага"!')

base = ['камень', 'ножницы', 'бумага']
computer_score = 0
user_score = 0
while True:
    my_choice = input(
        'Выберите: камень, ножницы, бумага или "стоп" для выхода: ').lower()
    if my_choice == 'стоп':
        print('Выход через 3...')
        t.sleep(1)
        print('2')
        t.sleep(1)
        print('1...')
        t.sleep(1)
        print('Вы вышли из игры! Еще увидимся!')
        break
    if my_choice not in base:
        print('Неверный выбор, попробуйте снова.')
        t.sleep(1)
        continue
    pc_choice = random.choice(base)
    print(f'Ваш выбор: {my_choice}, выбор компьютера: {pc_choice}')
    t.sleep(1)
    if my_choice == pc_choice:
        print('Ничья!')
    elif (my_choice == 'камень' and pc_choice == 'ножницы') or \
         (my_choice == 'ножницы' and pc_choice == 'бумага') or \
         (my_choice == 'бумага' and pc_choice == 'камень'):
        print('Вы выиграли!')
        user_score += 1
    else:
        print('Вы проиграли!')
        computer_score += 1
    score = input('Хотите узнать счет? (да\нет):  ').lower()
    if score == 'да':
        print(f'Ваш счет: {user_score}, счет компьютера: {computer_score}')
    elif score == 'нет':
        print('Хорошо, продолжим!')
    else:
        print('Неверный ввод, продолжим без счета.')
    print('Игра продолжается...')
