def get_func_kwargs(func, is_method=True):
    return func.func_code.co_varnames[
        int(is_method):func.func_code.co_argcount]


def get_class_bases(klass):
    bases = set(klass.__bases__)
    sub_bases = set()

    for base in bases:
        sub_bases.update(get_class_bases(base))

    bases.update(sub_bases)
    return bases
