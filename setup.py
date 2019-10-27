from setuptools import setup
from setuptools import find_packages

with open('README.md') as file:
    long_description = file.read()

version = '1.0.0'

# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.
install_requires = [
    'acme>=0.21.1',
    'certbot>=0.21.1',
    'requests',
    'mock',
    'setuptools',
    'zope.interface',
]

docs_extras = [
]

setup(
    name='certbot-dns-webservice',
    version=version,
    description="Webservice DNS Authenticator plugin for Certbot",
    url='https://github.com/bastig/certbot-dns-webservice',
    author="Sebastian Gmeiner",
    license='Apache License 2.0',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-webservice = certbot_dns_webservice.dns_webservice:Authenticator',
        ],
    },
    test_suite='certbot_dns_webservice',
)