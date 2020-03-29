
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'DjangoMpesa',
    version = '0.1',
    packages = ['DjangoMpesa'],
    include_package_data = True,
    license = 'BSD License',
    description = 'A simple Django app for integrating mpesa stk push payment to your django site.',
    long_description = README,
    url = 'http://www.techtenant.co.ke/',
    author = 'Oronz',
    author_email = 'brianoroni6@gmail.com',
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
        'Topic :: mpesa :: stk push :: payment'

    ]
)