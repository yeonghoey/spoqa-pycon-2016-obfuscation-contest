import re
import sys


c, t = dict(_=None), dict(_=(lambda _: re.findall('([\d.]+|[-+*/()])', _))(sys.argv[1]))
_, __ = (lambda: c['_'], lambda: c.update({'_':'_'}) if not t['_'] else (c.update({'_': t['_'][0]}), t.update({'_': (t['_'][1:])})))
__()

def expr():
    return repeat_expr(term())

def repeat_expr(r):
    global _, __
    l = _()
    a = list(map(lambda _: (__(), eval(str(r)+_+str(term()))), filter(lambda _: _ == l, '+-')))
    return repeat_expr(sum(map(lambda _: _[1], a))) if any(a) else r


def term():
    return repeat_term(factor())


def repeat_term(r):
    global _, __
    l = _()
    a = list(map(lambda _: (__(), eval(str(r)+_+str(factor()))), filter(lambda _: _ == l, '*/')))
    return repeat_term(sum(map(lambda _: _[1], a))) if any(a) else r


def factor():
    global _, __
    l = _()
    a = list(map(lambda _: (__(), eval(_+str(factor()))), filter(lambda _: _ == l, '+-')))
    if a: return sum(map(lambda _: _[1], a))

    f = lambda _: (__(), float(_.group(0))) if _ else (_, _)
    b, c = f(re.match(r'[\d.]+', l))
    if c: return c

    return (__(), expr(), (None() if _() != ')' else __()))[1] if l == '(' else None()


result = expr()
print(result) if _() == '_' else None()
