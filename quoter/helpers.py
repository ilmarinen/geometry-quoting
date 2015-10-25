from scipy.spatial import ConvexHull
import numpy as np
import consts


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
    sa = (a[0] - center[0], a[1] - center[1])
    extremals = [a]
    theta_zero = get_angle(sa)
    for i in xrange(num_quarters):
        theta = theta_zero + (i + 1) * (- np.pi / 2)
        extremal_point = ((radius * np.cos(theta)) + center[0], (radius * np.sin(theta)) + center[1])
        extremals.append(extremal_point)

    return extremals


def cost_circular_arc(circular_arc):
    length_arc = get_clockwise_arc_length(circular_arc.a, circular_arc.b, circular_arc.center, circular_arc.radius)
    machine_speed = consts.V_MAX * np.exp(-1 / circular_arc.radius)
    total_time = length_arc / machine_speed
    total_cost = total_time * consts.MTC
    return total_cost


def cost_line_segment(line_segment):
    length_line_segment = get_line_length(line_segment.a, line_segment.b)
    machine_speed = consts.V_MAX
    total_time = length_line_segment / machine_speed
    total_cost = total_time * consts.MTC
    return total_cost


def cost_stock(width, height):
    padded_stock_area = (width + consts.PADDING) * (height + consts.PADDING)
    total_cost = padded_stock_area * consts.MATERIAL_COST
    return total_cost


def make_quote(data):
    quote_stock = cost_stock(data['rectangle']['width'], data['rectangle']['height'])
    quote_lines = 0
    quote_arcs = 0
    for line_segment in data['line_segments'].values():
        quote_lines = quote_lines + cost_line_segment(line_segment)

    for circular_arc in data['circular_arcs'].values():
        quote_arcs = quote_arcs + cost_circular_arc(circular_arc)

    total_quote = quote_stock + quote_lines + quote_arcs

    return total_quote


def get_affine_transform_parameters(a, b):
    theta = np.arctan2(b[1] - a[1], b[0] - a[0])
    return [np.transpose(np.matrix((-a[0], -a[1]))), theta]


def affine_transform(v, theta, vertices):
    rotation_matrix = np.matrix([[np.cos(theta), -1 * np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    new_vertices = []
    for vertex in vertices:
        vertex_vec = np.transpose(np.matrix(vertex))
        new_vertex = rotation_matrix * (vertex_vec - v)
        new_vertices.append((new_vertex[0, 0], new_vertex[1, 0]))

    return new_vertices


def get_dimensions_rectangle(vertices, optimize=False):
    if not optimize:
        return get_dimensions_naive_rectangle(vertices)
    else:
        return get_dimensions_optimized_rectangle(vertices)


def get_dimensions_naive_rectangle(vertices):
    x_oords = [v[0] for v in vertices]
    y_oords = [v[1] for v in vertices]

    x_min = np.min(x_oords)
    x_max = np.max(x_oords)
    y_min = np.min(y_oords)
    y_max = np.max(y_oords)
    width = np.abs(x_max - x_min)
    height = np.abs(y_max - y_min)

    return [width, height]


def get_dimensions_optimized_rectangle(vertices):
    hull = ConvexHull(vertices)
    width, height = get_dimensions_naive_rectangle(vertices)
    min_area = width * height

    for i in xrange(len(hull.vertices)):
        a = vertices[hull.vertices[i]]
        b = vertices[hull.vertices[(i + 1) % len(hull.vertices)]]
        v, theta = get_affine_transform_parameters(a, b)
        transformed_vertices = affine_transform(v, theta, vertices)
        w, h = get_dimensions_naive_rectangle(transformed_vertices)
        area = w * h
        if area < min_area:
            min_area = area
            width = w
            height = h

    return width, height















