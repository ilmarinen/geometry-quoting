from opster import command, dispatch
from quoter.profile_parser import load_file
from quoter.helpers import make_quote


@command()
def quote(filepath=('f', '', 'Path to profile representation file'),
          optimize_rectangle=('', False, 'Optimize for the smallest rectangular\
            piece of stock which can contain the profile')):
    data = load_file(filepath, optimize=optimize_rectangle)
    print '{0:.2f}'.format(make_quote(data))


if __name__ == '__main__':
    dispatch()
