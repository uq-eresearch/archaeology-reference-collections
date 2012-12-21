from .models import Accession

from django.views.generic import DetailView, ListView, TemplateView


class AccessionListView(ListView):
    model = Accession


class AccessionDetailView(DetailView):
    model = Accession
    slug_field = 'uq_accession'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AccessionDetailView, self).get_context_data(**kwargs)
        # Add to the context
        woodfeatures = hasattr(self.object, 'woodfeatures')
        seedfeatures = hasattr(self.object, 'seedfeatures')
        context['woodfeatures'] = woodfeatures
        context['seedfeatures'] = seedfeatures

        # which should be active by default
        context['woodactive'] = 'active' if woodfeatures else ''
        context['seedactive'] = 'active' if seedfeatures and not woodfeatures else ''

        return context


class HomepageView(TemplateView):
    template_name = "botanycollection/index.html"
