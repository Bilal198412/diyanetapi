#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


def main_arg(*args):
    """docstring for main"""
    hlist = []
    for v in sorted(args):
        if hasattr(v, '__iter__'):
            result = {
                'tuple': lambda: v,
                'list': lambda: tuple(sorted(v)),
                'dict': lambda: tuple(sorted(v.items()))
            }[type(v).__name__]()
            hlist.append(result)
        else:
            hlist.append(v)
    return hash(tuple(hlist))


def main_kwarg(**kwargs):
    """docstring for main"""
    hlist = []
    for k, v in sorted(kwargs.iteritems()):
        if hasattr(v, '__iter__'):
            result = {
                'tuple': lambda: v,
                'list': lambda: tuple(sorted(v)),
                'dict': lambda: tuple(sorted(v.items()))
            }[type(v).__name__]()
            hlist.append(result)
        else:
            hlist.append((k, v))
    return hash(tuple(hlist))
# ----------------------------------------------------------------


def test_main():
    args = tuple([3, 1, dict(a=100), [3, 1], (99, 33)])

    kwargs = dict(a=1, b=10, c=dict(x=3, y=99), d=[1, 3])
    kw = main_kwarg(**kwargs)
    ar = main_arg(*args)
    assert ((ar + kw) == (kw + ar))


if __name__ == '__main__':
    test_main()
