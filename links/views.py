from django.urls import reverse_lazy
from django.views.generic import FormView
from links.forms import LinkForm


class LinkView(FormView):
    form_class = LinkForm
    template_name = 'link-add.html'
    success_url = reverse_lazy('links:link-add_view')
