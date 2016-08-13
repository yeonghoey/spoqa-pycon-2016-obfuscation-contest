import re


token_map = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiply',
    '/': 'divide',
    '(': 'lparen',
    ')': 'rparen'
}


def tokenize(s):
    symbols = ''.join(token_map)
    pattern = '([\d.]+|[%s])' % symbols
    for lexeme in re.findall(pattern, s):
        name = token_map.get(lexeme, 'number')
        yield (name, lexeme)


def expr(tokenizer):
    l = term(tokenizer)
    print l
    try:
        name, _ = next(tokenizer)
        print name
        if name == 'plus':
            r = term(tokenizer)
            return l + r
        if name == 'minus':
            r = term(tokenizer)
            return l - r
    except StopIteration:
        pass
    return l


def term(tokenizer):
    l = factor(tokenizer)
    print l
    try:
        name, _ = next(tokenizer)
        if name == 'multiply':
            r = factor(tokenizer)
            return l * r
        if name == 'divide':
            r = factor(tokenizer)
            return l / r
    except StopIteration:
        pass
    return l


def factor(tokenizer):
    name, lexeme = next(tokenizer)
    if name == 'number':
        return float(lexeme)

    if name == 'lparen':
        ret = expr(tokenizer)
        expect(tokenizer, 'rparen')
        return ret

    raise Exception()


def expect(tokenizer, expected):
    name, _ = next(tokenizer)
    if name != expected:
        return
    else:
        raise Exception()


if __name__ == '__main__':
    tests = [
        # '1 2 3',
        # '12 3',
        '1 + 2 + 3',
        # '1 * 2 - 3',
        # '(1 + 2) - 3)',
        # '1 - 2 * 3',
    ]
    for t in tests:
        print expr(tokenize(t))
