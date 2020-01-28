from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dserial',
    version='0.0.2',
    description='Python data serializer with type checking',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='pjongy',
    author_email='whdduq218@gmail.com',
    url='https://github.com/pjongy/dserial',
    install_requires=[],
    packages=find_packages(),
    keywords=['serialize', 'type'],
    python_requires='>=3.7',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ]
)
