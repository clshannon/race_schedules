from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import EventForm
from .models import Event


class EventList(ListView):
    model = Event
    paginate_by = 20


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:list')


class EventDetail(DetailView):
    model = Event


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:list')


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events:list')
