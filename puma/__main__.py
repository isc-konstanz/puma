#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
puma
~~~~

To learn how to use photovoltaic utility and manufacturing systems, see "puma --help"

"""

from argparse import ArgumentParser, RawTextHelpFormatter


os.environ["NUMEXPR_MAX_THREADS"] = str(os.cpu_count())


def main() -> None:
    import puma

    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {puma.__version__}")

    with puma.load(parser=parser) as application:
        application.main()


if __name__ == "__main__":
    main()
