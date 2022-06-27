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
    print('    ├── precedenceof() ... ', end='')

    assert(Parser.precedenceof('+') == 1)
    print(' 1 ', end='')

    assert(Parser.precedenceof('-') == 1)
    print(' 2 ', end='')

    assert(Parser.precedenceof('*') == 2)
    print(' 3 ', end='')

    assert(Parser.precedenceof('/') == 2)
    print(' 4 ', end='')

    # Unsupported operator raises ValueError
    try:
        Parser.precedenceof('**')
        assert(False)
    except ValueError:
        print(' 5 ', end='')

    print(' Passed!')

def test_evaluate():
    print('    └── evaluate() ... ', end='')

    for i in range(0, 1000):
        assert(Parser.evaluate(i, '+', i) == i + i)
    print(' 1 ', end='')

    for i in range(0, 1000):
        assert(Parser.evaluate(-i, '-', -i) == -i - -i)
    print(' 2 ', end='')

    for i in range(0, 10):
        assert(Parser.evaluate(i, '*', i) == i * i)
    print(' 3 ', end='')

    for i in range(1, 1000):
        assert(Parser.evaluate(i, '/', i) == i / i)
    print(' 4 ', end='')

    # Should not evaluate division by zero
    try:
        Parser.evaluate(0, '/', 0)
        assert(False)
    except ZeroDivisionError:
        print(' 5 ', end='')

    # Should not evaluate unsupported operators
    try:
        Parser.evaluate(i, '**', i)
        assert(False)
    except ValueError:
        print(' 6 ', end='')

    print(' Passed!')

def run():
    print('Testing parser.py ... ')
    test_precedenceof()
    test_evaluate()
    print('│   Passed!')
