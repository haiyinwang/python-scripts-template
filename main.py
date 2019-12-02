#!/usr/bin/env python
"""
A simple python script template.
"""
import os
import sys
import argparse

from dotenv import load_dotenv


def main(arguments):
    """
    Main function which takes command line arguments
    to manage control flow of the script
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('test-arg', help="Test argument", type=str)
    args = parser.parse_args(arguments)


if __name__ == '__main__':
    # Load .env file
    load_dotenv()
    sys.exit(main(sys.argv[1:]))