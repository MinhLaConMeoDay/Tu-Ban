from setuptools import setup

from meomeo import __version__

setup(
    name='meomeo',
    version=__version__,

    url='https://github.com/MinhLaConMeoDay/Tu-Ban',
    author='NhungChuMeoCon',
    author_email='anhnh.t1.1821@gmail.com',

    py_modules=['meomeo'],
    install_requires=[
        'numpy',

    ],
)
