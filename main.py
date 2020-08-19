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
        answ = input('\n -Ваша ставка?\n -Что бы выйти введите "Exit"\n').lower()
        if answ == 'exit':
            break

        result_player1 = throw()
        result_jav1st1 = throw()
        result_player2 = throw()
        result_jav1st2 = throw()
        score_player = result_player1 + result_player2
        score_jav1st = result_jav1st1 + result_jav1st2

        if result_jav1st1 == result_jav1st2:
            print("Компьютер выкинул дубль! Сумма выиграша умножена вдвое - ", score_jav1st * 2)
        elif result_player1 == result_player2:
            print("Поздравляю, у Вас дубль! Сумма выиграша умножена вдвое - ", score_player * 2)

        answ = int(answ)
        if answ <= int(balance.read_balance()):
            print(f'Вы выкинули', result_player1, "и", result_player2)
            print(f'Компьютер кинул', result_jav1st1, "и", result_jav1st2)
            if score_player > score_jav1st:
                print('Вы выиграли!')
                money = answ + balance.read_balance()
                print(f'Ваш баланс', money, 'монет')
                balance.write_balance(money)
                balance.read_balance()
            elif score_jav1st == score_player:
                print('Ничья!')
            else:
                print("Вы проиграли.")
                money = balance.read_balance() - answ
                print(f'Ваш баланс', money, 'монет')
                balance.write_balance(money)
        else:
            print('Неизвестная команда ')
            break


def start():
    answ = input("1)Продолжить игру\n2)Новая игра\n3)Выход\n")
    if answ == '2':
        balance.zero()
        game()
    elif answ == '3':
        exit()
    elif answ == '1':
        game()


start()
