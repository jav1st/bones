'''
Я ебал меня сосали
'''

start_money = 500


def read_balance():
    f = open('money.txt', 'r')
    return int(f.read())


def write_balance(money):
    f = open('money.txt', 'w')
    f.write(str(money))


def zero():
    f = open('money.txt', 'w')
    f.write(str(start_money))
