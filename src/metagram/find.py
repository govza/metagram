#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main metagrams computing script
"""
import argparse
import os
import sys
from collections import defaultdict


class Metagram:
    dictionary_graph = defaultdict(list)

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.get_dictionary(first, last)
        print(self.dictionary_graph)

    def get_dictionary(self, first, last):
        '''Creates dictionary of words with length of words given
        where key is word and value is list where edges can be added'''

        assert len(first) == len(last), \
            u"Length of both words should be the same"

        with open(f"{os.path.dirname(__file__)}/words.txt") as filehandle:
            for line in filehandle:
                word_from_file = line[:-1]
                if len(word_from_file) == len(first):
                    self.dictionary_graph[word_from_file]


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
