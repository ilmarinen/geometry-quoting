import numpy as np
from quoter import helpers
from quoter.profile_parser import load_file


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
    assert np.abs((helpers.get_clockwise_arc_length((1, 0), (0, 1), (1, 1), 1)) - (np.pi / 2)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((0, 1), (1, 0), (1, 1), 1)) - (3 * np.pi / 2)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((1, 2), (1, 0), (1, 1), 1)) - (np.pi)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((1, 0), (1, 2), (1, 1), 1)) - (np.pi)) < 0.00001
    assert np.abs((helpers.get_clockwise_arc_length((1, 0), (1, 0), (1, 1), 1)) - (2 * np.pi)) < 0.00001


def test_get_line_length():
    assert np.abs(helpers.get_line_length((1, 1), (0, 1)) - 1) < 0.00001
    assert np.abs(helpers.get_line_length((1, 0), (0, 1)) - np.sqrt(2)) < 0.00001
    assert np.abs(helpers.get_line_length((0, 0), (1, 1)) - np.sqrt(2)) < 0.00001


def test_arc_extremals():
    extremals = helpers.get_extremal_points_of_arc((0, 1), (0, -1), (0, 0), 1)
    assert len(extremals) == 3
    a = extremals[0]
    b = extremals[1]
    c = extremals[2]
    assert helpers.get_line_length(a, (0, 1)) < 0.00001 or helpers.get_line_length(a, (1, 0)) < 0.00001 or helpers.get_line_length(a, (0, -1)) < 0.00001
    assert helpers.get_line_length(b, (0, 1)) < 0.00001 or helpers.get_line_length(b, (1, 0)) < 0.00001 or helpers.get_line_length(b, (0, -1)) < 0.00001
    assert helpers.get_line_length(c, (0, 1)) < 0.00001 or helpers.get_line_length(c, (1, 0)) < 0.00001 or helpers.get_line_length(c, (0, -1)) < 0.00001

    extremals = helpers.get_extremal_points_of_arc((0, 2), (2, 0), (0, 0), 2)
    assert len(extremals) == 2
    a = extremals[0]
    b = extremals[1]
    assert helpers.get_line_length(a, (0, 2)) < 0.00001 or helpers.get_line_length(a, (2, 0)) < 0.00001
    assert helpers.get_line_length(b, (0, 2)) < 0.00001 or helpers.get_line_length(b, (2, 0)) < 0.00001

    extremals = helpers.get_extremal_points_of_arc((2, 1), (2, 0), (2, 0.5), 0.5)
    assert len(extremals) == 3
    a = extremals[0]
    b = extremals[1]
    c = extremals[2]
    assert helpers.get_line_length(a, (2, 1)) < 0.00001 or helpers.get_line_length(a, (2, 0)) < 0.00001 or helpers.get_line_length(a, (2.5, 0.5)) < 0.00001
    assert helpers.get_line_length(b, (2, 1)) < 0.00001 or helpers.get_line_length(b, (2, 0)) < 0.00001 or helpers.get_line_length(b, (2.5, 0.5)) < 0.00001


def test_optimized_rectangle():
    vertices = [(0.0, 0.0), (0.0, 3.0), (5.0, 3.0), (5.0, 0.0)]
    v = np.transpose(np.matrix((1, 1)))
    theta = np.pi / 4
    transformed_vertices = helpers.affine_transform(v, theta, vertices)
    width, height = helpers.get_dimensions_optimized_rectangle(transformed_vertices)
    optimized_area = width * height
    width, height = helpers.get_dimensions_naive_rectangle(transformed_vertices)
    naive_area = width * height
    assert np.abs(optimized_area - 15.0) < 0.00001
    assert np.abs(naive_area - 15.0) > 0.00001


def test_make_quote():
    data_rect = load_file('./examples/Rectangle.json')
    data_extrude_circular_arc = load_file('./examples/ExtrudeCircularArc.json')
    data_circular_arc = load_file('./examples/CircularArc.json')
    assert '{0:.2f}'.format(helpers.make_quote(data_rect)) == '14.10'
    assert '{0:.2f}'.format(helpers.make_quote(data_extrude_circular_arc)) == '4.47'
    assert '{0:.2f}'.format(helpers.make_quote(data_circular_arc)) == '4.06'

    data_rect = load_file('./examples/Rectangle.json', optimize=True)
    data_extrude_circular_arc = load_file('./examples/ExtrudeCircularArc.json', optimize=True)
    data_circular_arc = load_file('./examples/CircularArc.json', optimize=True)
    assert '{0:.2f}'.format(helpers.make_quote(data_rect)) == '14.10'
    assert '{0:.2f}'.format(helpers.make_quote(data_extrude_circular_arc)) == '4.47'
    assert '{0:.2f}'.format(helpers.make_quote(data_circular_arc)) == '4.06'

    data_missing_corners = load_file('./examples/MissingCorners.json')
    assert '{0:.2f}'.format(helpers.make_quote(data_missing_corners)) == '15.41'
