import re
import sys


globals().update({
    'tokenize': lambda _: re.findall('([\d.]+|[-+*/()])', _),
})


def tokenizer(stream):
    t = tokenize(stream)
    c = None
    def g(): return c
    def n():
        nonlocal t, c
        c, t = ('eol', t) if not t else (t[0], t[1:])
    return g, n


def expr(g, n):
    r = term(g, n)
    return repeat_expr(g, n, r)

def repeat_expr(g, n, r):
    l = g()
    a = list(map(lambda _: (n(), eval(str(r)+_+str(term(g, n)))), filter(lambda _: _ == l, '+-')))
    return repeat_expr(g, n, sum(map(lambda _: _[1], a))) if any(a) else r


def term(g, n):
    ret = factor(g, n)
    while True:
        l = g()
        if l == '*':
            n()
            ret = ret * factor(g, n)
        elif l == '/':
            n()
            ret = ret / factor(g, n)
        else:
            break
    return ret


def factor(g, n):
    l = g()
    if l == '+':
        n()
        return factor(g, n)
    if l == '-':
        n()
        return -factor(g, n)
    m = re.match(r'[\d.]+', l)
    if m is not None:
        n()
        return float(m.group(0))

    if l == '(':
        n()
        ret = expr(g, n)
        if g() != ')':
            raise Exception()
        n()
        return ret

    raise Exception()


if __name__ == '__main__':
    g, n = tokenizer(sys.argv[1])
    try:
        n()
        result = expr(g, n)
        l = g()
        if l == 'eol':
            print(result)
        else:
            raise Exception()
    except StopIteration:
        pass
    except Exception as e:
        print(e)
        sys.exit(1)
