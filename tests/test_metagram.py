#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from metagram import Metagram

__author__ = "Rasul Akhmatkhanov"
__copyright__ = "Rasul Akhmatkhanov"
__license__ = "mit"


def test_metagramm():
    metagram = Metagram("top", "map")
    assert metagram == ["top", "tap", "map"]
