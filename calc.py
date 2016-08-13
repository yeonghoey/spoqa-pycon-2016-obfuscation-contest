import re
import sys


def _(stream):
    t, c = dict(_=(lambda _: re.findall('([\d.]+|[-+*/()])', _))(stream)), dict(_=None)
    return (lambda: c['_'], lambda: c.update({'_':'_'}) if not t['_'] else (c.update({'_': t['_'][0]}), t.update({'_': (t['_'][1:])})))


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
__()
result = expr(_, __)
print(result) if _() == '_' else None()
