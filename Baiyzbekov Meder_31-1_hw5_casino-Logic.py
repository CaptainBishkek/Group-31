import random

def logic(number, amount):
    win_number = random.randint(1, 30)
    if number == win_number:
        print(f'Вы выиграли! {amount * 2}')
        return amount * 2 

    else:
        print(f'Число на табло {win_number}')
        print(f'Вы проиграли! Ваш текущий бюджет{-amount}')
        return -amount