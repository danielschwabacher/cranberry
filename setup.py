from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '1.0.3'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='cranberry',
    entry_points={
        'console_scripts':[
            'cranberry = cranberry.__main__:main'
        ]
    },
    version=__version__,
    description='An automated music downloading service',
    long_description=long_description,
    url='https://github.com/danielschwabacher/cranberry',
    download_url='https://github.com/danielschwabacher/cranberry/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='automation music youtube-dl',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Daniel Schwabacher',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='danielschwabacher@gmail.com'
)
