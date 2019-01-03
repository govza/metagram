#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main metagrams computing script
"""
import argparse
import os
import sys


class Metagram:
    def __init__(self, first, last):
        self.first = first
        self.last = last


def find(words):
    metagram = str(Metagram(words[0], words[1]))
    return metagram


def parse_args(args):
    parser = argparse.ArgumentParser(
        description="Metagrams finding script")
    parser.add_argument(
        'words', metavar='N', type=str, nargs='*', help='a strings')
    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls
    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    assert len(args.words) == 2, "Specify two words to build chain"

    print(f"The metagrams are {find(args.words)}.")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
