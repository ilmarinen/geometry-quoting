import numpy as np


def get_angle(vertex):
    x = vertex[0]
    y = vertex[1]

    theta = np.arctan2(y, x)
    if theta > 0:
        theta = theta - (2 * np.pi)

    return theta


def get_clockwise_arc_length(a, b, center=None, radius=None):
    if center is None:
        raise Exception('No Center', 'You need to specify a point to use as the center')

    if radius is None:
        raise Exception('No Radius', 'You need to specify the radius of your arc')

    if a == b:
        return (2 * np.pi * radius)
    else:
        ca = (a[0] - center[0], a[1] - center[1])
        cb = (b[0] - center[0], b[1] - center[1])
        theta_a = get_angle(ca)
        theta_b = get_angle(cb)

        if theta_b <= theta_a:
            return np.abs((theta_b - theta_a) * radius)
        else:
            return np.abs((2 * np.pi - (theta_b - theta_a)) * radius)
