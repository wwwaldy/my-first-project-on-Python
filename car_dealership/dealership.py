import cars_base
import time
from typing import Dict


def display_welcome_message() -> None:
    """Отображает приветственное сообщение."""
    print('\nДобро пожаловать в автосалон!')
    print('У нас есть автомобили Audi A, RS и Q серий.\n')


def check_car_systems() -> None:
    """Имитирует проверку систем автомобиля."""
    systems = ['давление в шинах', 'уровень масла',
               'уровень охлаждающей жидкости']
    for system in systems:
        time.sleep(1)
        print(f'Проверяем {system}...\n')


def display_car_info(car: Dict) -> None:
    """Отображает информацию об автомобиле."""
    print(
        f"Вы выбрали Audi {car['model'].title()} {car['year']} {car['color'].title()}.")
    for info in ['price', 'engine', 'mileage']:
        time.sleep(0.3)
        print(f"{info.title()}: {car[info]}")


def exit_program() -> None:
    """Отображает сообщение о выходе с обратным отсчетом."""
    print('Спасибо за покупку!')
    print('Выход через...')
    for i in range(3, 0, -1):
        time.sleep(1)
        print(i)
    time.sleep(1)


def get_car_series() -> str:
    """Запрашивает у пользователя серию автомобиля."""
    return input('Введите название серии (A, RS, Q): ').lower()


def get_car_model(series: str) -> str:
    """Запрашивает у пользователя модель автомобиля."""
    series_models = {
        'a': 'A(В наличии модели A4, A5, A7)',
        'rs': 'RS(В наличии модели RS4, RS5, RS7)',
        'q': 'Q(В наличии модели Q3, Q5, Q8)'
    }
    return input(f'Введите название модели {series_models[series]}: \n').lower()


def get_car_data(series: str, model: str) -> Dict:
    """Получает данные об автомобиле из базы данных."""
    car_series = {
        'a': cars_base.audi_a_series,
        'rs': cars_base.audi_rs_series,
        'q': cars_base.audi_q_series
    }
    return car_series[series].get(model)


def continue_shopping() -> bool:
    """Спрашивает пользователя о продолжении покупок."""
    response = input('Вы хотите продолжить? (Y/N): ').lower()
    if response == 'y':
        return True
    elif response == 'n':
        exit_program()
        return False
    else:
        print('Некорректный ввод. Попробуйте еще раз.')
        return False


def main():
    """Основная функция программы."""
    while True:
        display_welcome_message()
        series = get_car_series()

        if series not in ['a', 'rs', 'q']:
            print('Неверная серия. Попробуйте еще раз.')
            continue

        model = get_car_model(series)
        car = get_car_data(series, model)

        if not car:
            print('Модель не найдена.')
            continue

        check_car_systems()
        display_car_info(car)

        if not continue_shopping():
            break


if __name__ == '__main__':
    main()
