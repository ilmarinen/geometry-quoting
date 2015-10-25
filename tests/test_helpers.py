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
    assert np.abs((helpers.get_angle(v1) * 180 / np.pi) - 0.0) < 0.00001
    assert np.abs((helpers.get_angle(v2) * 180 / np.pi) - -45.0) < 0.00001
    assert np.abs((helpers.get_angle(v3) * 180 / np.pi) - -90.0) < 0.00001
    assert np.abs((helpers.get_angle(v4) * 180 / np.pi) - - 135.0) < 0.00001
    assert np.abs((helpers.get_angle(v5) * 180 / np.pi) - -180.0) < 0.00001
    assert np.abs((helpers.get_angle(v6) * 180 / np.pi) - -225.0) < 0.00001
    assert np.abs((helpers.get_angle(v7) * 180 / np.pi) - -270.0) < 0.00001
    assert np.abs((helpers.get_angle(v8) * 180 / np.pi) - -315.0) < 0.00001


def test_get_clockwise_arc_length():
    assert np.abs((helpers.get_clockwise_arc_length((1, 0), (0, 1), center=(1, 1), radius=1)) - (np.pi / 2)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((0, 1), (1, 0), center=(1, 1), radius=1)) - (3 * np.pi / 2)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((1, 2), (1, 0), center=(1, 1), radius=1)) - (np.pi)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((1, 0), (1, 2), center=(1, 1), radius=1)) - (np.pi)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((1, 0), (1, 0), center=(1, 1), radius=1)) - (2 * np.pi)) < 0.00001
