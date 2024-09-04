from django.db.models import Q
from django.views.generic import ListView

from .models import Person


class PersonListView(ListView):
    model = Person
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page'] = self.request.GET.get('page', 1)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(email__icontains=search)
            )

        return queryset
