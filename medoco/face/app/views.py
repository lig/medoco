from django.views.generic import TemplateView


__all__ = ['DashView', 'TypeView', 'TypeListView', 'TypeDeleteView']


class MedocoAjaxView(TemplateView):
    pass


class DashView(TemplateView):
    template_name = 'medoco/dash.html'


class TypeView(MedocoAjaxView):
    pass


class TypeListView(MedocoAjaxView):
    template_name = 'medoco/type_list.html'


class TypeDeleteView(MedocoAjaxView):
    pass
