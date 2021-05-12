import math


def check(to_check):
    for item in to_check:
        if item[2] < 0.001:
            return False
    return True


def move_to_zero(target, zero):
    return target[0] - zero[0], target[1] - zero[1]


def get_path(x, y):
    return math.sqrt(x * x + y * y)


def get_angel_of(left, center, right):
    if not check((left, center, right)):
        return -1

    x1, y1 = move_to_zero(left, center)
    x2, y2 = move_to_zero(right, center)
    l1 = get_path(x1, y1)
    l2 = get_path(x2, y2)
    dot_product = x1 * x2 + y1 * y2
    cos = dot_product / (l1 * l2)
    return math.degrees(math.acos(cos))
