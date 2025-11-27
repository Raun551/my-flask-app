from setuptools import setup, find_packages

setup(
    name='my-flask-app',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask==3.0.0',
        'pytest==7.4.3',
        'pytest-flask==1.3.0',
    ],
)
