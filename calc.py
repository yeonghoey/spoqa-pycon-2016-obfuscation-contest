import re
import sys


def _(stream):
    t, c = [(lambda _: re.findall('([\d.]+|[-+*/()])', _))(stream)], [None]
    g = lambda: c[0]
    def ____():
        c[0], t[0] = ('_', t) if not t[0] else (t[0][0], t[0][1:])
        return ____
    return g, ____


def expr(g, n):
    r = term(g, n)
    return repeat_expr(g, n, r)

def repeat_expr(g, n, r):
    l = g()
    a = list(map(lambda _: (n(), eval(str(r)+_+str(term(g, n)))), filter(lambda _: _ == l, '+-')))
    return repeat_expr(g, n, sum(map(lambda _: _[1], a))) if any(a) else r


def term(g, n):
    r = factor(g, n)
    return repeat_term(g, n, r)


def repeat_term(g, n, r):
    l = g()
    a = list(map(lambda _: (n(), eval(str(r)+_+str(factor(g, n)))), filter(lambda _: _ == l, '*/')))
    return repeat_term(g, n, sum(map(lambda _: _[1], a))) if any(a) else r


def factor(g, n):
    l = g()
    a = list(map(lambda _: (n(), eval(_+str(factor(g, n)))), filter(lambda _: _ == l, '+-')))
    if a: return sum(map(lambda _: _[1], a))

    f = lambda _: (n(), float(_.group(0))) if _ else (_, _)
    b, c = f(re.match(r'[\d.]+', l))
    if c: return c

    return (n(), expr(g, n), (None() if g() != ')' else n()))[1] if l == '(' else None()


_, __ = _(sys.argv[1])
result = expr(_, __())
print(result) if _() == '_' else None()
