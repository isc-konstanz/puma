#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    puma
    ~~~~

    To learn how to use photovoltaic utility and manufacturing systems, see "puma --help"

"""
import os
from argparse import ArgumentParser, RawTextHelpFormatter

import puma


def main() -> None:
    with puma.load(parser=_get_parser()) as application:
        if application.settings["action"] == "run":
            application.run()
        elif application.settings["action"] == "start":
            application.start()
            application.wait()


def _get_parser() -> ArgumentParser:
    from puma import __version__

    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s {version}".format(version=__version__))

    subparsers = parser.add_subparsers(dest="action")
    # subparsers.required = True
    subparsers.default = "run"
    subparsers.add_parser("run", help="run local resources, connectors and systems")
    subparsers.add_parser("start", help="start the local resource system")

    return parser


if __name__ == "__main__":
    main()
