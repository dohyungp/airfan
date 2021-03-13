from setuptools import find_packages, setup

setup(
    name='airpan',
    version='0.0.1',
    description='Airflow operator and sensor plugins',
    long_description=open('README.md').read(),
    url='https://github.com/dohyungp/airfan',
    author='Dohyung Park',
    author_email='dohyung.prk@gmail.com',
    maintainer='Dohyung Park',
    maintainer_email='dohyung.prk@gmail.com',
    license='MIT License',
    packages=find_packages(exclude=['tests']),
    install_requires=open('requirements.txt').read().split('\n'),
)
