import helpers


class LineSegment(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


class CircularArc(object):

    def __init__(self, a, b, center):
        self.center = center
        self.a = a
        self.b = b
        self.radius = helpers.get_line_length(center, a)
