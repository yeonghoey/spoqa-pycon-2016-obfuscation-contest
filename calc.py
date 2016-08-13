import re
import sys


def ___(______, _______, ________):
    _____ = list(map(lambda _: _[1], list(map(lambda _: (globals()['__'](), eval(str(______)+_+str(eval(_______)))), list(filter(lambda __: __ == globals()['_'](), ________))))))
    return ___(sum(_____), _______, ________) if _____ else ______


def ____():
    l = globals()['_']()
    _____ = list(map(lambda _: (globals()['__'](), eval(_+str(____()))), filter(lambda _: _ == l, '+-')))
    if _____: return sum(map(lambda _: _[1], _____))

    f = lambda _: (globals()['__'](), float(_.group(0))) if _ else (_, _)
    b, c = f(re.match(r'[\d.]+', l))
    if c: return c

    return (globals()['__'](), ___(___(____(), '____()', '*/'), '___(____(), "____()", "*/")', '+-'), (None() if globals()['_']() != ')' else globals()['__']()))[1] if l == '(' else None()


c, t = dict(_=None), dict(_=(lambda _: re.findall('([\d.]+|[-+*/()])', _))(sys.argv[1]))
_, __ = (lambda: c['_'], lambda: c.update({'_':'_'}) if not t['_'] else (c.update({'_': t['_'][0]}), t.update({'_': (t['_'][1:])})))
__(); ______ = ___(___(____(), '____()', '*/'),  '___(____(), "____()", "*/")', '+-')
print(______) if _()=='_' else None()
