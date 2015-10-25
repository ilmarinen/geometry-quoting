import numpy as np
from quoter import helpers


v1 = (1, 0)
v2 = (1, -1)
v3 = (0, -1)
v4 = (-1, -1)
v5 = (-1, 0)
v6 = (-1, 1)
v7 = (0, 1)
v8 = (1, 1)


def test_get_angle():
    assert (helpers.get_angle(v1) * 180 / np.pi) == 0.0
    assert (helpers.get_angle(v2) * 180 / np.pi) == -45.0
    assert (helpers.get_angle(v3) * 180 / np.pi) == -90.0
    assert (helpers.get_angle(v4) * 180 / np.pi) == - 135.0
    assert (helpers.get_angle(v5) * 180 / np.pi) == -180.0
    assert (helpers.get_angle(v6) * 180 / np.pi) == -225.0
    assert (helpers.get_angle(v7) * 180 / np.pi) == -270.0
    assert (helpers.get_angle(v8) * 180 / np.pi) == -315.0
