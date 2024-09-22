from math import sqrt
from colorama import Fore
# coef
variants =[ 
    [0.2, -300],
    [0.3, -200],
    [0.1, -100],
    [0.4, -400]
]


def find_M():
    return variants[0][0] * variants[0][1] + variants[1][0] * variants[1][1] + variants[2][0] * variants[2][1]

def find_SSV(M):
    return sqrt(variants[0][0] * (variants[0][1] - M) **2 + variants[1][0] * (variants[1][1] - M) **2)

def find_CSV(ssv, M):
    return ssv/M

def main():
    print("-- Оцінка ефективності проектів --")
    print("Значення семіквадратичне відхилення -", find_SSV(find_M()))
    print( "Коефіцієнт семіваріації -", find_CSV(find_SSV(find_M()), find_M()))
    print()

main()