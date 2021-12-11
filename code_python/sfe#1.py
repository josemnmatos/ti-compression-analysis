from copy import copy
from math import log2, ceil

from prefixcode import isprefixcode


def shannon_fano_elias(probability, sort_symbols=False):
    symbols = list(probability.keys())

    # sort symbols for execution stability
    if sort_symbols:
        symbols.sort()

    def F(i):
        a = sum(probability[k] for k in symbols[:i])
        b = probability[symbols[i]] / 2
        return a + b

    def L(symbol):
        p = probability[symbol]
        return ceil(-log2(p)) + 1

    def Z(x, n):
        x = round(x, 7)  # avoid rounding error
        assert(0 <= x <= 1)
        if x == 1:
            return '0' * n

        z = ''
        for i in range(1, n+1):
            if x >= pow(2, -i):
                x -= pow(2, -i)
                z += '1'
            else:
                z += '0'
        return z

    return {symbol: Z(F(i), L(symbol)) for i, symbol in enumerate(symbols)}


def test_shannon_fano_elias():
    probability = {"A": 1/3, "B": 1/4, "C": 1/6, "D": 1/4}
    code = shannon_fano_elias(probability, sort_symbols=True)
    expected = {"A": "001", "B": "011", "C": "1010", "D": "111"}
    assert(code == expected)
    assert(isprefixcode(code))


if __name__== 'main':
    test_shannon_fano_elias()


