import setuptools


with open('README.md', 'rt', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='muslang',
    version='0.0.1',
    author='Maxim Soukharev',
    author_email='maxim.soukharev@gmail.com',
    description='Musical language',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/msoukharev/muslang',
    project_urls={
        'Bug Tracker': 'https://github.com/msoukharev/muslang/issues',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic',
        'Topic :: Compilers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10'
    ],
    package_dir={'': '.'},
    packages=setuptools.find_packages(where='.'),
    python_requires='>=3.10',
    install_requires=['mingus', 'pytest']
)
