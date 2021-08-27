import random
import balance

'''
1) Приветствие игрока
2) Запрос броска игрока
3) Бросок компьютера 
4) Результаты бросков
'''


def throw():
    numbers = (1, 2, 3, 4, 5, 7)
    return random.choice(numbers)


def game():
    while True:
        answ = input('\n -Ваша ставка?\n -Что бы выйти введите "Exit"\n -Узнать баланс- введите "Balance"\n').lower()
        if answ == 'exit':
            break
        if answ == 'balance':
            print(balance.read_balance())
            continue

        result_player1 = throw()
        result_jav1st1 = throw()
        result_player2 = throw()
        result_jav1st2 = throw()
        score_player = result_player1 + result_player2
        score_jav1st = result_jav1st1 + result_jav1st2
        double_player = ' '
        double_jav1st = ' '

        if result_jav1st1 == result_jav1st2:
            score_jav1st = score_jav1st * 2
            double_jav1st = True
            double_jav1st = f'\nКомпьютер выкинул дубль! Сумма выиграша умножена вдвое -  {score_jav1st}'

        elif result_player1 == result_player2:
            score_player = score_player * 2
            double_player = True
            double_player = f'\nПоздравляю, у Вас дубль! Сумма выиграша умножена вдвое - {score_player}'

        answ = int(answ)
        print(f'Ваша ставка {answ} монет')

        if answ <= int(balance.read_balance()):
            print(f'Вы выкинули', result_player1, 'и', result_player2, double_player)
            print(f'Компьютер кинул', result_jav1st1, 'и', result_jav1st2, double_jav1st)
            if score_player > score_jav1st:
                print('Вы выиграли!')
                money = answ + balance.read_balance()
                print(f'Вам зачислоно {answ} монет.\nВаш баланс {money} монет')
                balance.write_balance(money)
                balance.read_balance()
                continue

            elif score_jav1st == score_player:
                print('Ничья!')
                continue

            else:
                print("Вы проиграли.")
                money = balance.read_balance() - answ
                print(f'Списано {answ} монет.\nВаш баланс {money} монет')
                balance.write_balance(money)
                if money == 0:
                    zero_balance()
                continue

        if answ >= int(balance.read_balance()):
            print(f'Ваш баланс {balance.read_balance()}'
                  f'\nУменьшите ставку')
            continue

        else:
            print('Неизвестная команда ')
            break


def start():
    answ = input('''Приветствую! Это игра в кости. Правила просты- побеждает тот, у кого выпало наибольшее число.
Бросок двух производится поочерёдно, одинаковое значение умножается вдвое.
 1)Продолжить игру\n 2)Новая игра\n 3)Выход\n''')
    if answ == '2':
        balance.zero()
        game()
    elif answ == '3':
        exit()
    elif answ == '1':
        game()


def zero_balance():
    answ = input('Вы проиграли все деньги! Начать новую игру?.\n Да\Нет\n').lower()
    if answ == 'да':
        balance.zero()
        game()
    if answ == 'нет':
        print('До скорых встреч!')
        exit()


start()
