import json


class Player:

    start_money = 500
    def __init__(self, name):
        self.name = name
        self.money = 500

    def player_read(self):
        with open(f'{self.name}.json', 'r', encoding='utf-8') as out:
            self.data = json.load(out)

    def player_write(self):
        player_stats = {'Вас зовут': self.name,
                        'На вашем счету': self.money}
        with open(f'{self.name}.json', 'w', encoding='utf-8') as into:
            json.dump(player_stats, into)

    def zero(self):
        data =  self.player_read()
        del data


#    def read_balance:
#        f = open('money.txt', 'r')
#        return int(f.read())
#
#    def write_balance(money):
#        f = open('money.txt', 'w')
#        f.write(str(money))
#
