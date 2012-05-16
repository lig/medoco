from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView


__all__ = ['DashView', 'TypeView', 'TypeListView', 'TypeDeleteView']


class MedocoAjaxView(TemplateView):

    def dispatch(self, request, *args, **kwargs):

        if not request.is_ajax():
            base_url = reverse('medoco_dash')
            medoco_url = request.path_info.replace(base_url, '/', 1)
            return redirect('%s#%s' % (base_url, medoco_url))

        return super(MedocoAjaxView, self).dispatch(request, *args, **kwargs)


class DashView(TemplateView):
    template_name = 'medoco/dash.html'


class TypeView(MedocoAjaxView):
    pass


class TypeListView(MedocoAjaxView):
    template_name = 'medoco/type_list.html'


class TypeDeleteView(MedocoAjaxView):
    pass
