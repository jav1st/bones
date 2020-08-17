import random
import balance

'''
1) Приветствие игрока
2) Запрос броска игрока
3) Бросок компьютера 
4) Результаты бросков
'''

numbers = (1, 2, 3, 4, 5, 7)


def throw():
    return random.choice(numbers)


def game():

    result_player = throw()
    result_jav1st = throw()

    answ = input('Ставка, сука? ').lower()
    answ = int(answ)
    if answ <= int(balance.read_balance()):
        print(f'Вы выкинули', result_player)
        print(f'Кудахтер кинул', result_jav1st)
        if result_player > result_jav1st:
            print('Вы выиграли! Идите на хуй!')
            money = answ + balance.read_balance()
            print(f'Ваш баланс', money, 'хуёв')
            balance.write_balance(money)
            balance.read_balance()
        elif result_jav1st == result_player:
            print('Ничья, идите на хуй оба!')
        else:
            print("Ты проебал. Иди на хуй!")
            money = balance.read_balance() - answ
            print(f'Ваш баланс', money, 'хуёв')
            balance.write_balance(money)
    else:
        print('Иди на хуй')


def start():
    answ = input("Начать новую или продолжить?").lower()
    if answ == 'новая':
        balance.zero()
    game()

start()
