#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
twinline
~~~~~~~~

To learn how to use photovoltaic production line twins, see "twinline --help"

"""

import os
from argparse import ArgumentParser, RawTextHelpFormatter

os.environ["NUMEXPR_MAX_THREADS"] = str(os.cpu_count())


def main() -> None:
    import twinline

    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {twinline.__version__}")

    application = twinline.load(parser=parser)
    application.main()


if __name__ == "__main__":
    main()
