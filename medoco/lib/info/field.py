from ..util import get_func_kwargs, get_class_bases


class FieldInfo(object):

    def __init__(self, klass):
        self.klass = klass
        self.name = klass.__name__

        attrs = set()
        attrs.update(get_func_kwargs(klass.__init__.__func__))

        for base in get_class_bases(klass):
            if hasattr(base.__init__, '__func__'):
                attrs.update(get_func_kwargs(base.__init__.__func__))

        self.attrs = list(attrs)
