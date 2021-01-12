from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.contrib import messages
from links.forms import LinkForm
from links.models import Link


class LinkView(FormView):
    form_class = LinkForm
    template_name = 'link-add.html'
    success_url = reverse_lazy('links:link-add-view')

    def form_valid(self, form):
        obj = None

        try:
            obj = Link.objects.get(
                long_url=form.cleaned_data['long_url']
            )
        except Link.DoesNotExist:
            obj = Link(long_url=form.cleaned_data['long_url'])
            obj.save()

        short_url = f'{self.request.scheme}://{self.request.get_host()}/{obj.id}'
        messages.add_message(self.request, messages.INFO, f'Twój krótki link to: <a target="_blank" href="{short_url}">{short_url}</a>')

        return super().form_valid(form)


def RedirView(request, pk, *args):
    try:
        p = Link.objects.get(pk=pk)
    except Link.DoesNotExist:
        raise Http404('URL nie istnieje.')

    return HttpResponseRedirect(p.long_url)
