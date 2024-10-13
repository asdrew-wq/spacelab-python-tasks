def f(zombies, plants):
    # Солдати, що вижили
    z_points, p_points = 0, 0

    # Якщо одне із значень відсутнє (різна довжина масивів), солдат з непустим значенням виживає
    diff = len(zombies) - len(plants)
    if diff > 0:
        z_points += diff
    else:
        p_points -= diff

    # Кожен елемент масиву атакує елемент іншого масиву з тим самим індексом масиву.
    # Той, хто вижив, - це число з найбільшим значенням.
    n = min(len(zombies), len(plants))
    for i in range(n):
        if zombies[i] > plants[i]:
            z_points += 1
        elif zombies[i] < plants[i]:
            p_points += 1

    if z_points == p_points:
        return True if sum(plants) >= sum(zombies) else False
    return True if p_points > z_points else False


if __name__ == '__main__':
    tests = ({'zombies': [1, 3, 5, 7], 'plants': [2, 4, 6, 8]},
            {'zombies': [1, 3, 5, 7], 'plants': [2, 4]},
            {'zombies': [1, 3, 5, 7], 'plants': [2, 4, 0, 8]},
            {'zombies': [2, 1, 1, 1], 'plants': [1, 2, 1, 1]})

    for test in tests:
        print(f(test['zombies'], test['plants']))
