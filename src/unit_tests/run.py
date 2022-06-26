from . import test_parser

def run():
    print('Running unit test ...')
    print('└── ', end='')
    test_parser.run()
    print('Unit test complete!')

run()
