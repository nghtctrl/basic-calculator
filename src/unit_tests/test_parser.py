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

from ..parser.parser import Parser

def test_precedenceof():
    print('    └── precedenceof() ... ', end='')

    assert(Parser.precedenceof('+') == 1)
    print(' 1 ', end='')

    assert(Parser.precedenceof('-') == 1)
    print(' 2 ', end='')

    assert(Parser.precedenceof('*') == 2)
    print(' 3 ', end='')

    assert(Parser.precedenceof('/') == 2)
    print(' 4 ', end='')

    # Precedence of a currently unsupported operator
    assert(Parser.precedenceof('**') == 0)
    print(' 5 ', end='')

    print(' Passed!')

def run():
    print('Testing parser.py ... ')
    test_precedenceof()
    print('│   Passed!')
