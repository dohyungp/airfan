from setuptools import find_packages, setup

setup(
    name='airpan',
    version='0.0.1',
    python_requires=">=3.5",
    classifiers=[
        "OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
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
