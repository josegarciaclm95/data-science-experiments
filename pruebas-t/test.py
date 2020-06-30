def f_rank(iterable, start=1):
    """Fractional ranking"""
    enum_arr = enumerate(iterable, 1)
    last, equals = None, []
    final_rank = []
    for index, elem in enum_arr:
        if elem != last and len(equals) != 0:
            avg = sum([i for i, _ in equals]) / len(equals)
            final_rank += map(lambda x: (avg, x[1]), equals)
            equals = []
        last = elem
        equals.append((index, elem))
    if len(equals) != 0:
        avg = sum([i for i, _ in equals]) / len(equals)
        final_rank += map(lambda x: (avg, x[1]), equals)
    return final_rank

scores = [3, 5, 5, 5, 5, 8]
print(f_rank(scores))