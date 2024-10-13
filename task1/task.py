def f(sides):
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    return False


if __name__ == '__main__':
    abc = input('Введіть a, b, c через пробіл: ')
    while abc.startswith(' '):
        abc = abc[1:]
    while abc.endswith(' '):
        abc = abc[:-1]
    try:
        abc = [eval(i) for i in abc.split(' ')]
        abc.sort()
        assert len(abc) == 3
        if f(abc):
            print('Це сторони трикутика Піфагора')
        else:
            print('Це не сторони трикутика Піфагора')
    except (TypeError, AssertionError, NameError):
        print('Потрібно ввести три числа')
