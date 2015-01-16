from setuptools import setup, find_packages


setup(
    name='cs399-band',
    version='0.1.0',
    description='CS399 Band',
    long_description=open('README.rst').read(),
    keywords=[
        'class',
        'django',
        'nau'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/justin/cs399',
    download_url='https://github.com/justin/cs399/archive/master.zip',
    packages=find_packages(),
    license='UNLICENSE',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
