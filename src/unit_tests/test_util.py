#!/usr/bin/env python3

# Copyright (C) 2022 Jiho Kim (nghtctrl@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from ..parser.util import isnumber

def test_isnumber():
    print('    └── isnumber() ... ', end='')

    for i in range(0, 1000):
        assert(isnumber(str(i)))
    print(' 1 ', end='')

    for i in range(0, 1000):
        assert(isnumber(str(-i)))
    print(' 2 ', end='')

    for i in range(0, 1000):
        assert(isnumber(str(float(i) + 0.1)))
    print(' 3 ', end='')

    for i in range(0, 100):
        assert(isnumber(str(float(-i) - 0.1)))
    print(' 4 ', end='')

    assert(isnumber(str(6.0221415e+23)))
    print(' 5 ', end='')

    print(' Passed!')

def run():
    print('Testing util.py ... ')
    test_isnumber()
    print('    Passed!')
