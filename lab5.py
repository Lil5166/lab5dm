F = [1, 0, 1, 0, 0, 1, 1, 1]
print("F = " + str(F))
# print('x y z F')
# for x in range(2):
#     for y in range (2):
#         for z in range(2):
#             print(x,y,z)
#             for F in range(2):
print(' X  Y  Z  F')
truthTable = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
for row in truthTable:
    print(row)


def main():
    dualFunction_selfdual(F)
    DDNF(F)
    DKNF(F)
    ZhegalkinPolynomial_lineal(F)
    print("Функція зберігає константу 0: " + str(Const0(F)))
    print("Функція зберігає константу 1: " + str(Const1(F)))
    print("Функція монотонна: " + str(Monoton(F)))


def dualFunction_selfdual(F):
    result = False
    reversedF = reversed(F)
    dualFunction = []
    for i in reversedF:
        if i == 0:
            dualFunction.append(1)
        else:
            dualFunction.append(0)
    print("Двоїста функція: " + str(dualFunction))
    if dualFunction == F:
        result = True
    print("Функція самодвоїста:  " + str(result))


# def polynomial(F):


def Const0(F):
    result = True
    for f in F:
        if f == 1:
            result = False
    return result


def Const1(F):
    result = True
    for f in F:
        if f == 0:
            result = False
    return result


def Monoton(F):
    result = False
    sortedArray = sorted(F)
    if sortedArray == F:
        result = True
    return result


def DDNF(F):
    print("Досконала диз'юнктивна нормальна форма")

    ddnf = 'f(x1, x2, x3) = '
    for i in range(len(truthTable)):
        if truthTable[i][3] == 1:
            ddnf += '('
            for j in range(len(truthTable[i]) - 1):
                if truthTable[i][j] == 1:
                    ddnf += ('x' + str(j + 1))
                else:
                    ddnf += ('¬x' + str(j + 1))

                if j + 1 != 3:
                    ddnf += str(' ∧ ')

            ddnf += ') v '

    newDdnf = ddnf[:len(ddnf) - 3]

    print(newDdnf)


def DKNF(F):
    print("Досконала кон’юнктивна нормальна форма")

    dknf = 'f(x1, x2, x3) = '
    for i in range(len(truthTable)):
        if truthTable[i][3] == 0:
            dknf += '('
            for j in range(len(truthTable[i]) - 1):
                if truthTable[i][j] == 0:
                    dknf += ('x' + str(j + 1))
                else:
                    dknf += ('¬x' + str(j + 1))

                if j + 1 != 3:
                    dknf += str(' v ')

            dknf += ') ∧ '

    newDknf = dknf[:len(dknf) - 3]

    print(newDknf)


def ZhegalkinPolynomial_lineal(F):
    print("Поліном Жегалкіна")
    zhegalkinPolynomial = 'f(x1, x2, x3) = '
    for i in range(len(truthTable)):
        if truthTable[i][3] == 1:
            zhegalkinPolynomial += '('
            for j in range(len(truthTable[i]) - 1):
                if truthTable[i][j] == 1:
                    zhegalkinPolynomial += ('x' + str(j + 1))
                else:
                    zhegalkinPolynomial += ('x' + str(j + 1) + ' ⊕ 1')

                if j + 1 != 3:
                    zhegalkinPolynomial += str(' ∧ ')

            zhegalkinPolynomial += ') ⊕ '

    newZhegalkinPolynomial = zhegalkinPolynomial[:len(zhegalkinPolynomial) - 3]

    print(newZhegalkinPolynomial)

    linal1 = "∧"
    if linal1 in newZhegalkinPolynomial:
        print("Функція не лінійна")
    else:
        print("Функція лінійна")


main()
