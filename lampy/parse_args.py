import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--system-packages', nargs="+", default=[])
    parser.add_argument('--shared-objects', nargs="+", default=[])
    parser.add_argument('--bundle-name', default='bundle.zip')
    parser.add_argument('--source-directory', default='/home/ec2-user/project')
    parser.add_argument('--bundle-destination', default='/home/ec2-user')
    parser.add_argument('--zip-lib-dir', default='lib')

    return parser
