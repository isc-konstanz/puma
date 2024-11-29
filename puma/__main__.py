#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
puma
~~~~

To learn how to use photovoltaic utility and manufacturing systems, see "puma --help"

"""

from argparse import ArgumentParser, RawTextHelpFormatter

import puma


def _get_parser() -> ArgumentParser:
    from puma import __version__

    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s {version}".format(version=__version__))

    return parser


if __name__ == "__main__":
    with puma.load(parser=_get_parser()) as application:
        application.main()
