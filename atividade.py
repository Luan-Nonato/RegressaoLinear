import matplotlib.pyplot as plt
import csv
import math
from random import randint

dice = []
with open("AnaliseEstudo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        if row[0] != "Idade":
            average = (int(row[3]) + int(row[4]) + int(row[5])) / 3
            aux = {
                "Idade": row[0],
                "TempoEstudo": row[1],
                "Faltas": row[2],
                "MediaProvas": average
            }
            dice.append(aux)
N = len(dice)
for type in ["Idade", "TempoEstudo", "Faltas"]:
    self.get_modelo(dice, type, i)

def get_modelo(self, dice, type, i):
    s_dice = self.split_dados(dice, type)
    training, test = self.split_bases(s_dice, i)
    B0, B1 = self.regressao_linear(training, type)
    xs = [d[0] for d in s_dice]
    ys_r = [(B0 + (d[0] * B1)) for d in s_dice]
    desvio = self.calc_desvio(test, B0, B1)
    print("Desvio padrão: " + str(desvio))
    plt.title('Média das Provas x ' + type)
    plt.xlabel(type.title())
    plt.ylabel('Média das provas')
    plt.plot(xs, ys_r)
    plt.show()

#Provavelmente esse calculo de desvio está incorreto
def calc_desvio(self, test, B0, B1):
    detour = 0
    for i in test:
        y = i[1]
        fx = (B0 + (i[0] * B1))
        detour += (y - fx) ** 2
    return detour


def regressao_linear(self, training, type):
    N = len(training)
    s_x = self.somat(training, 'x')
    s_y = self.somat(training, 'y')
    s_xy = self.somat(training, 'xy')
    s_x2 = self.somat(training, 'x2')
    B1 = ((s_x * s_y) - (N * s_xy)) / ((s_x ** 2) - (N * s_x2))
    B0 = (s_y - (B1 * s_x)) / N
    print(type + ": y = " + str(B0) + " + " + str(B1) + "x")
    return B0, B1


def somatorio(self, numbers_list, type):
    numbers = []
    for i in numbers_list:
        if type == 'x':
            a = i[0]
        elif type == 'y':
            a = i[1]
        elif type == 'xy':
            a = i[0] * i[1]
        elif type == 'x2':
            a = i[0] ** 2
        else:
            a = 1
            print('Se fudeu')
        numbers.append(a)
    return sum(numbers)


def split_bases(self, dice, i):
    positions = []
    while (len(positions) < round(i * 0.7)):
        position = randint(0, i - 1)
        if position not in positions:
            positions.append(position)
    training = [dice[p] for p in positions]
    test = [dice[p] for p in range(len(dice)) if p not in positions]
    return training, test


def split_dados(self, dice, type):
    result = []
    for item in dice:
        if type == "Idade":
            x = item.get("Idade")
        elif type == "TempoEstudo":
            x = item.get("TempoEstudo")
        elif type == "Faltas":
            x = item.get("Faltas")
        y = item.get("MediaProvas")
        result.append((int(x), int(y)))
    return result