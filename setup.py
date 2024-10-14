from distutils.core import setup

setup(
    name='PyMsTeamsAdaptiveCard',
    version='0.1.8',
    author='Florian Salaun',
    author_email='florian.salaun@gmail.com',
    packages=['pyadaptivecard', 'pyadaptivecard.test'],
    scripts=[],
    url='http://pypi.python.org/pypi/PyMsTeamsAdaptiveCard/',
    license='LICENSE.txt',
    description='Generate Microsoft Teams Adaptive Cards for new Connectors',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "requests >= 2.32.2"
    ],
)