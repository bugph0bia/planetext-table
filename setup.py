import setuptools

from __version__ import __version__


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='planetext_table',
    version=__version__,
    author='bugph0bia',
    author_email='',
    description='planetext table generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bugph0bia/planetext-table',
    packages=setuptools.find_packages(),
    license='MIT',
    keywords='',
    classifiers=[
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
    ],
    install_requires=[
    ],
)
