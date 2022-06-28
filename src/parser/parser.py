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

from .util import isnumber

class Parser:
    # Expression must be in a string in a list, not just a string
    def __init__(self, expression):
        self.expression = expression

    def calculate(self):
        output_queue = []
        operator_stack = []

        for token in self.expression:
            if isnumber(token):
                try:
                    output_queue.append(int(token))
                except ValueError:
                    output_queue.append(float(token))
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    op = operator_stack.pop()
                    rhs = output_queue.pop()
                    lhs = output_queue.pop()
                    output_queue.append(evaluate(lhs, op, rhs))
                operator_stack.pop()
            else:
                if len(operator_stack) != 0 and precedenceof(operator_stack[-1]) >= precedenceof(token):
                    op = operator_stack.pop()
                    rhs = output_queue.pop()
                    lhs = output_queue.pop()
                    output_queue.append(evaluate(lhs, op, rhs))
                operator_stack.append(token)

        while len(operator_stack) != 0:
            op = operator_stack.pop()
            rhs = output_queue.pop()
            lhs = output_queue.pop()
            output_queue.append(evaluate(lhs, op, rhs))

        return output_queue[-1]

    @staticmethod
    def precedenceof(op):
        if op == '*' or op == '/':
            return 2
        elif op == '+' or op == '-':
            return 1
        else:
            raise ValueError('unsupported operator')

    @staticmethod
    def evaluate(lhs, op, rhs):
        if op == '+':
            return lhs + rhs
        elif op == '-':
            return lhs - rhs
        elif op == '*':
            return lhs * rhs
        elif op == '/':
            return lhs / rhs
        else:
            raise ValueError('unsupported operator')
