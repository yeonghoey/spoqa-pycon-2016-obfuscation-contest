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

class Tokenizer(object):
    def __init__(self, stream):
        self.tokens = iter(tokenize(stream))
        self.current = None

    def next(self):
        try:
            self.current = next(self.tokens)
        except StopIteration:
            self.current = 'eol'
        return self.current


def expr(g, n):
    ret = term(g, n)
    while True:
        lexeme = g()
        if lexeme == '+':
            n()
            ret = ret + term(g, n)
        elif lexeme == '-':
            n()
            ret = ret - term(g, n)
        else:
            break
    return ret


def term(g, n):
    ret = factor(g, n)
    while True:
        lexeme = g()
        if lexeme == '*':
            n()
            ret = ret * factor(g, n)
        elif lexeme == '/':
            n()
            ret = ret / factor(g, n)
        else:
            break
    return ret


def factor(g, n):
    lexeme = g()
    if lexeme == '+':
        n()
        return factor(g, n)
    if lexeme == '-':
        n()
        return -factor(g, n)
    m = re.match(r'[\d.]+', lexeme)
    if m is not None:
        n()
        return float(m.group(0))

    if lexeme == '(':
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
        lexeme = g()
        if lexeme == 'eol':
            print(result)
        else:
            raise Exception()
    except StopIteration:
        pass
    except Exception as e:
        print(e)
        sys.exit(1)
