# -*- coding:utf-8 -*-
# Problema 1805
# Authors: Fabián Camp Mussa

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = iter([int(x) for x in stdin.read().split()])

a = next(nums)
b = next(nums)

print ((a+b) + (a-b) + (b+a) + (b-a))
