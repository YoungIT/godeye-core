from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = [line.strip() for line in f]

setup(
    name='src',
    version='0.1.0',
    description='God eye cant find your love',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ae tao yitec",
    url='https://github.com/YoungIT/godeye-core',
    packages=find_packages(),
    install_requires=install_requires
)