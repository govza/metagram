#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from metagram.find import Metagram


def test_metagramm():
    metagram = Metagram("top", "map")
    assert metagram.shortest_path == ['top', 'mop', 'map']
