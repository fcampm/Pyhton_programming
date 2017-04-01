# -*- coding:utf-8 -*-
# Problema 1102
# Authors: Fabián Camp Mussa

from __future__ import print_function
from __future__ import division

from sys import stdin

nums = [int(x) for x in stdin.read().split()]

for i in range(len(nums)):
    if nums[i] % 11 == 0 and nums[i] != 0:
        print (nums[i], "is a multiple of 11.")
    elif nums[i] % 11 != 0 and nums[i] != 0:
        print (nums[i], "is not a multiple of 11.")
