import re
import sys


globals().update({
    'tokenize': lambda _: iter(re.findall('([\d.]+|[-+*/()])', _)),
})


class Tokenizer(object):
    def __init__(self, stream):
        self.tokens = tokenize(stream)
        self.current = None

    def next(self):
        try:
            self.current = next(self.tokens)
        except StopIteration:
            self.current = 'eol'
        return self.current


def expr(tokenizer):
    ret = term(tokenizer)
    while True:
        lexeme = tokenizer.current
        if lexeme == '+':
            tokenizer.next()
            ret = ret + term(tokenizer)
        elif lexeme == '-':
            tokenizer.next()
            ret = ret - term(tokenizer)
        else:
            break
    return ret


def term(tokenizer):
    ret = factor(tokenizer)
    while True:
        lexeme = tokenizer.current
        if lexeme == '*':
            tokenizer.next()
            ret = ret * factor(tokenizer)
        elif lexeme == '/':
            tokenizer.next()
            ret = ret / factor(tokenizer)
        else:
            break
    return ret


def factor(tokenizer):
    lexeme = tokenizer.current
    if lexeme == '+':
        tokenizer.next()
        return factor(tokenizer)
    if lexeme == '-':
        tokenizer.next()
        return -factor(tokenizer)
    m = re.match(r'[\d.]+', lexeme)
    if m is not None:
        tokenizer.next()
        return float(m.group(0))

    if lexeme == '(':
        tokenizer.next()
        ret = expr(tokenizer)
        if tokenizer.current != ')':
            raise Exception()
        tokenizer.next()
        return ret

    raise Exception()


if __name__ == '__main__':
    tokenizer = Tokenizer(sys.argv[1])
    try:
        tokenizer.next()
        result = expr(tokenizer)
        lexeme = tokenizer.current
        if lexeme == 'eol':
            print(result)
        else:
            raise Exception()
    except StopIteration:
        pass
    except Exception as e:
        print(e)
        sys.exit(1)
