from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from forms import TypeForm


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
    template_name = 'medoco/type.html'

    def get_context_data(self, **kwargs):

        if 'type_id' in kwargs:
            pass
        else:

            if self.request.method == 'POST':
                type_form = TypeForm(self.request.POST)

                if type_form.is_valid():
                    pass

            else:
                type_form = TypeForm()

        return {'type_form': type_form}


class TypeListView(MedocoAjaxView):
    template_name = 'medoco/type_list.html'


class TypeDeleteView(MedocoAjaxView):
    pass
