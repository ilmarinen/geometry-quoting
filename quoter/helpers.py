import numpy as np


def get_angle(vertex):
    x = vertex[0]
    y = vertex[1]

    theta = np.arctan2(y, x)
    if theta > 0:
        theta = theta - (2 * np.pi)

    return theta


def get_clockwise_angle(a, b, center):
    if a == b:
        return (2 * np.pi)
    else:
        ca = (a[0] - center[0], a[1] - center[1])
        cb = (b[0] - center[0], b[1] - center[1])
        theta_a = get_angle(ca)
        theta_b = get_angle(cb)

        if theta_b <= theta_a:
            return (theta_b - theta_a)
        else:
            return (2 * np.pi - (theta_b - theta_a))


def get_clockwise_arc_length(a, b, center, radius):
    return np.abs(get_clockwise_angle(a, b, center) * radius)


def get_line_length(a, b):
    x_a = a[0]
    y_a = a[1]
    x_b = b[0]
    y_b = b[1]
    sum_squares = (x_b - x_a) ** 2 + (y_b - y_a) ** 2

    return np.sqrt(sum_squares)


def get_extremal_points_of_arc(a, b, center, radius):
    num_quarters = int(np.ceil(np.abs(get_clockwise_angle(a, b, center) / (np.pi / 2))))
    extremals = [a]
    theta_zero = get_angle(a)
    for i in xrange(num_quarters):
        theta = theta_zero + (i + 1) * (- np.pi / 2)
        extremal_point = (radius * (np.cos(theta) + center[0]), radius * (np.sin(theta) + center[1]))
        extremals.append(extremal_point)

    return extremals
