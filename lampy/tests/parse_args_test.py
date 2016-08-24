import unittest

from lampy import parse_args

class ParseArgsTest(unittest.TestCase):

    def setUp(self):
        self.parser = parse_args.get_parser()

    def test_argparse_defaults(self):
        args = []
        args = self.parser.parse_args(args)
        self.assertEqual(args.system_packages, [])
        self.assertEqual(args.shared_objects, [])
        self.assertEqual(args.bundle_name, 'bundle.zip')
        self.assertEqual(args.source_directory, '/home/ec2-user/project')
        self.assertEqual(args.bundle_destination, '/home/ec2-user')
        self.assertEqual(args.zip_lib_dir, 'lib')

    def test_argparse_system_packages(self):
        args = ['--system-packages', 'awesome-package', 'neat-thing']
        args = self.parser.parse_args(args)
        self.assertEqual(args.system_packages, ['awesome-package', 'neat-thing'])

    def test_argparse_shared_objects(self):
        args = ['--shared-objects', 'awesome.so', 'neat.so']
        args = self.parser.parse_args(args)
        self.assertEqual(args.shared_objects, ['awesome.so', 'neat.so'])

    def test_argparse_bundle_name(self):
        args = ['--bundle-name', 'banana.zip']
        args = self.parser.parse_args(args)
        self.assertEqual(args.bundle_name, 'banana.zip')

    def test_argparse_source_directory(self):
        args = ['--source-directory', '/some/place']
        args = self.parser.parse_args(args)
        self.assertEqual(args.source_directory, '/some/place')

    def test_argparse_bundle_destination(self):
        args = ['--bundle-destination', '/somewhere/else']
        args = self.parser.parse_args(args)
        self.assertEqual(args.bundle_destination, '/somewhere/else')

    def test_argparse_zip_lib_dir(self):
        args = ['--zip-lib-dir', 'so']
        args = self.parser.parse_args(args)
        self.assertEqual(args.zip_lib_dir, 'so')

if __name__ == '__main__':
    unittest.main()
