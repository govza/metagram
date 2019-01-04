#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main metagrams computing script
"""
import argparse
import os
import sys
from collections import defaultdict, deque


class Metagram:
    dictionary_graph = defaultdict(list)
    shortest_path = []

    def __str__(self):
        return ", ".join(self.shortest_path)

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.get_dictionary(first, last)
        self.add_edges_to_dictionary()
        self.shortest_path = self.find_shortest_path()

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

    def add_edges_to_dictionary(self):
        '''Add edges from word to word with only one letter difference'''
        for word in self.dictionary_graph:
            for comparison_word in self.dictionary_graph:
                if word is comparison_word:
                    continue
                else:
                    same_letters = 0
                    for idx, char in enumerate(word):
                        '''Check if words have same letters in same postions'''
                        if char == comparison_word[idx]:
                            same_letters += 1
                    if same_letters == len(word) - 1:
                        '''If only one letter difference add word to list'''
                        self.dictionary_graph[word].append(comparison_word)

    def find_shortest_path(self):
        '''Find shortest path from first to last in graph,
        using bread-first search.'''

        visited = {self.first: None}
        queue = deque([self.first])

        while queue:
            node = queue.popleft()
            if node == self.last:
                path = []
                while node is not None:
                    path.append(node)
                    node = visited[node]
                return path[::-1]

            for neighbour in self.dictionary_graph[node]:
                if neighbour not in visited:
                    visited[neighbour] = node
                    queue.append(neighbour)
        return queue


def find(words):
    metagram = Metagram(words[0], words[1])
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
