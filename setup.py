from distutils.core import setup

setup(
    name='aptivate-templatetags',
    version='0.1.0',
    author='Aptivate',
    author_email='carers+templatetags@aptivate.org',
    packages=['aptivate-templatetags', 'aptivate-templatetags.test'],
    url='http://pypi.python.org/pypi/aptivate-templatetags/',
    license='LICENSE.txt',
    description='A set of templatetags to extend Django',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.2",
    ],
)
