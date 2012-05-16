from django.template.base import Library, Node, TemplateSyntaxError, kwarg_re
from django.utils.encoding import smart_str


register = Library()


class MedocoURLNode(Node):
    def __init__(self, view_name, args, kwargs):
        self.view_name = view_name
        self.args = args
        self.kwargs = kwargs

    def render(self, context):
        from django.core.urlresolvers import reverse
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_str(k, 'ascii'), v.resolve(context))
                       for k, v in self.kwargs.items()])
        return reverse(self.view_name, urlconf='medoco.face.app.urls',
            args=args, kwargs=kwargs)


@register.tag
def medoco_url(parser, token):
    """
    Returns an URL relative to the medoco dash for hash based dash navigation
    """

    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument"
                                  " (path to a view)" % bits[0])
    viewname = bits[1]
    args = []
    kwargs = {}
    bits = bits[2:]

    for bit in bits:
        match = kwarg_re.match(bit)
        if not match:
            raise TemplateSyntaxError(
                "Malformed arguments to medoco url tag")
        name, value = match.groups()
        if name:
            kwargs[name] = parser.compile_filter(value)
        else:
            args.append(parser.compile_filter(value))

    return MedocoURLNode(viewname, args, kwargs)
