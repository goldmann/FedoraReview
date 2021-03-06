#!/usr/bin/env python
"""
Setup script
"""

from distutils.core import setup
from src.FedoraReview import __version__


setup(
    name = 'fedora-review',
    description = 'Tools to help review packages for inclusion in Fedora',
    description_long = '',
    data_files = [('/usr/share/man/man1/', [ 'fedora-review.1', 'fedora-create-review.1' ] ) ],
    version = __version__,
    license = 'GPLv2+',
    download_url = 'https://fedorahosted.org/releases/F/e/FedoraReview/',
    url = 'https://fedorahosted.org/FedoraReview/',
    package_dir = {'FedoraReview': 'src/FedoraReview'},
    packages = ['FedoraReview', 'FedoraReview.checks'],
    scripts=["src/fedora-review", "src/fedora-create-review"],
    )
