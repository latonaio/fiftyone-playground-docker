from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='fiftyone-playground-docker',
    version='',
    packages=[''],
    url='',
    license='',
    author='',
    author_email='',
    description='',
    install_requires=_requires_from_file('requirements.txt'),
)
