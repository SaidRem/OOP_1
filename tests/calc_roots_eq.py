def discriminant(a, b, c):
    """
    Функция для нахождения дискриминанта.
    """
    return b**2 - 4*a*c


def solution(a, b, c):
    """
    Функция для нахождения корней уравнения.
    """
    disc = discriminant(a, b, c)
    if disc < 0:
        res = "корней нет"
        return res
    elif disc == 0:
        x1 = (-b + disc**0.5)/(2*a)
        return x1
    else:
        x1 = (-b + disc**0.5)/(2*a)
        x2 = (-b - disc**0.5)/(2*a)
        return x1, x2


if __name__ == '__main__':
    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))
    print(solution(0, 2, -4))
