import json
import helpers
from profile_pieces import LineSegment, CircularArc


def load_file(filename, optimize=False):
    pfile = open(filename, 'r')
    pfile_data = json.loads(pfile.read().replace('\n', ''))
    vertices = {}
    edges = {}
    circular_arcs = {}
    extremal_points = []

    for v_name, v_center in pfile_data['Vertices'].iteritems():
        vertex = (v_center['Position']['X'], v_center['Position']['Y'])
        vertices[v_name] = vertex

    for e_name, e_data in pfile_data['Edges'].iteritems():
        if e_data['Type'] == 'LineSegment':
            a = vertices[str(e_data['Vertices'][0])]
            b = vertices[str(e_data['Vertices'][1])]
            edge = LineSegment(a, b)
            edges[e_name] = edge

        elif e_data['Type'] == 'CircularArc':
            circular_vertices = map(str, e_data['Vertices'])
            a = vertices[str(e_data['ClockwiseFrom'])]
            a_index = circular_vertices.index(str(e_data['ClockwiseFrom']))
            del(circular_vertices[a_index])
            b = vertices[circular_vertices[0]]
            center = (e_data['Center']['X'], e_data['Center']['Y'])
            circular_arc = CircularArc(a, b, center)
            circular_arcs[e_name] = circular_arc
            for v in helpers.get_extremal_points_of_arc(circular_arc.a, circular_arc.b, circular_arc.center, circular_arc.radius):
                extremal_points.append(v)

    width, height = helpers.get_dimensions_rectangle(vertices.values() + extremal_points, optimize=optimize)

    return {
        'vertices': vertices,
        'line_segments': edges,
        'circular_arcs': circular_arcs,
        'rectangle': {
            'width': width,
            'height': height
        }
    }
