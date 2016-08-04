from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ActivityForm
from .models import Activity


class ActivityList(ListView):
    model = Activity
    paginate_by = 20


class ActivityCreate(CreateView):
    model = Activity
    form_class = ActivityForm
    success_url = reverse_lazy('activities:list')


class ActivityDetail(DetailView):
    model = Activity


class ActivityUpdate(UpdateView):
    model = Activity
    form_class = ActivityForm
    success_url = reverse_lazy('activities:list')


class ActivityDelete(DeleteView):
    model = Activity
    success_url = reverse_lazy('activities:list')
