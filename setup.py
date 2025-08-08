#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
twinline
~~~~

Legacy compatibility setup script for the twinline package.

"""

import versioneer
from setuptools import setup

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
