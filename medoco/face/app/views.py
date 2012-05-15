from django.views.generic import TemplateView


__all__ = ['DashView']


class DashView(TemplateView):
    template_name = 'medoco/dash.html'
