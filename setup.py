from setuptools import setup

setup(
    name='example',
    version='0.1.0',
    py_modules=['example'],
    install_requires=[
        'pandas',
    ],
    entry_points='''
        [console_scripts]
        example=example:example
    ''',
)
