from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from forms import DocumentSpecForm


__all__ = ['DashView', 'DocSpecView', 'DocSpecListView', 'DocSpecDeleteView']


class MedocoAjaxView(TemplateView):

    def dispatch(self, request, *args, **kwargs):

        if not request.is_ajax():
            base_url = reverse('medoco_dash')
            medoco_url = request.path_info.replace(base_url, '/', 1)
            return redirect('%s#%s' % (base_url, medoco_url))

        return super(MedocoAjaxView, self).dispatch(request, *args, **kwargs)


class DashView(TemplateView):
    template_name = 'medoco/dash.html'


class DocSpecView(MedocoAjaxView):
    template_name = 'medoco/doc_spec.html'

    def get_context_data(self, **kwargs):

        if 'doc_spec_id' in kwargs:
            pass
        else:

            if self.request.method == 'POST':
                doc_spec_form = DocumentSpecForm(self.request.POST)

                if doc_spec_form.is_valid():
                    pass

            else:
                doc_spec_form = DocumentSpecForm()

        return {'doc_spec_form': doc_spec_form}


class DocSpecListView(MedocoAjaxView):
    template_name = 'medoco/doc_spec_list.html'


class DocSpecDeleteView(MedocoAjaxView):
    pass
