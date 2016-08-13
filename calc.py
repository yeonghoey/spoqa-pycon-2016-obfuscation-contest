import re
import sys


def ___(r, sub, ops):
    a = list(map(lambda _: (globals()['__'](), eval(str(r)+_+str(eval(sub)))), list(filter(lambda __: __ == globals()['_'](), ops))))
    return ___(sum(map(lambda _: _[1], a)), sub, ops) if any(a) else r


def ____():
    global _, __
    l = _()
    a = list(map(lambda _: (globals()['__'](), eval(_+str(____()))), filter(lambda _: _ == l, '+-')))
    if a: return sum(map(lambda _: _[1], a))

    f = lambda _: (globals()['__'](), float(_.group(0))) if _ else (_, _)
    b, c = f(re.match(r'[\d.]+', l))
    if c: return c

    return (globals()['__'](), ___(___(____(), '____()', '*/'), '___(____(), "____()", "*/")', '+-'), (None() if _() != ')' else globals()['__']()))[1] if l == '(' else None()


c, t = dict(_=None), dict(_=(lambda _: re.findall('([\d.]+|[-+*/()])', _))(sys.argv[1]))
_, __ = (lambda: c['_'], lambda: c.update({'_':'_'}) if not t['_'] else (c.update({'_': t['_'][0]}), t.update({'_': (t['_'][1:])})))
__(); r = ___(___(____(), '____()', '*/'),  '___(____(), "____()", "*/")', '+-')
print(r) if _()=='_' else None()
