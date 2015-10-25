from opster import command, dispatch
from quoter.profile_parser import load_file
from quoter.helpers import make_quote


@command()
def quote(filepath=('f', '', 'Path to profile representation file')):
    data = load_file(filepath)
    print '{0:.2f}'.format(make_quote(data))


if __name__ == '__main__':
    dispatch()
