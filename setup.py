try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'https://github.com/modulis/sccp_refcount.git',
    'download_url': 'https://github.com/modulis/sccp_refcount.git',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose','pyst2'],
    'packages': ['sccp_refcount'],
    'scripts': ['bin/sccp_refcount'],
    'name': 'sccp_refcount'
}

setup(**config)
