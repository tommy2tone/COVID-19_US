from setuptools import setup, find_packages


requires = [
    'pandas',
    'matplotlib'
]


setup(
    name='covid-19_US',
    version='0.0',
    description='covid-19_US',
    classifiers=[
        'Programming Language :: Python',
    ],
    author='Tom Hildebrand',
    author_email='thomas.hildebrand1@gmail.com',
    url='',
    keywords='python pandas matplotlib covid-19',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,

)
