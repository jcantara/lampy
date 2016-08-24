from setuptools import setup

setup(
    name='lampy',
    version='0.0.1',
    description='Python bundler for AWS Lambda',
    url='http://github.com/jcantara/lampy',
    author='Jesse Cantara',
    author_email='jcantara@gmail.com',
    license='MIT',
    packages=['lampy'],
    test_suite='nose.collector',
    tests_require=['nose'],
)
