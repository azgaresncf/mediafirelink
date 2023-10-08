from setuptools import setup, find_packages

setup(
    name='mediafirelink',
    version='1.0.0',
    description='A package for extracting download links from Mediafire URLs',
    author='azgaresncf',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)
