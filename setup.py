from setuptools import setup, find_packages

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, 'README.md'), encoding='utf-8') as readme:
    desc = readme.read()

setup(
    name='qsreplace',
    version='0.0.1',
    description='A utility to replace query parameters in URLs',
    long_description=desc,
    long_description_content_type='text/markdown',
    author='basedygt',
    license='Apache-2.0 License',
    author_email='basedygt@gmail.com',
    url='https://github.com/basedygt/qsreplace',
    packages=find_packages(),
    keywords=['qsreplace', 'url editor', 'params editor'],
    install_requires=['urllib3'],
)
