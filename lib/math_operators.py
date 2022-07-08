def get_human_readable_operator(op):
    if op == '>':
        return 'is bigger than'
    elif op == '<=':
        return 'is less or equals'
    elif op == '<':
        return 'is less than'
    elif op == '<':
        return 'is bigger or equals'
    elif op == '=' or op == '==':
        return 'equals'


def get_comparator(op):
    opers = {
        '>': lambda a, b: a > b,
        '>=': lambda a, b: a >= b,
        '<': lambda a, b: a < b,
        '<=': lambda a, b: a <= b,
        '==': lambda a, b: a == b
    }

    return opers[op]
