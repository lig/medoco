class FieldInfo(object):

    def __init__(self, klass):
        self.klass = klass
        self.name = klass.__name__
        self.attrs = []
