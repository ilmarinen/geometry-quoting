import numpy as np


def get_angle(vertex):
    x = vertex[0]
    y = vertex[1]

    theta = np.arctan2(y, x)
    if theta > 0:
        theta = theta - (2 * np.pi)

    return theta
