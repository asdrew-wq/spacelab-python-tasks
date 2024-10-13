def f(a, b, c):
    return a, b, c


if __name__ == '__main__':
    abc = input('Введіть a, b, c через пробіл: ')
    try:
        a, b, c = abc.split(' ')
    except ValueError:
        print('Потрібно ввести три числа')
    else:
        print(f(a, b, c))
