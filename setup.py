#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
puma
~~~~

Legacy compatibility setup script for the puma package.

"""

import versioneer
from setuptools import setup

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
