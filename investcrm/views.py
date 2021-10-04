from django.urls import reverse_lazy
import datetime
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Contact

class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'
    template_name_suffix = '_add'
    success_url = reverse_lazy('contact-list')

class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('contact-list')

class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contact-list')

class ContactListView(ListView):
    model = Contact
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        return context
