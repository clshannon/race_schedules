from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import RacetrackForm
from .models import Racetrack


class RacetrackList(ListView):
    model = Racetrack
    paginate_by = 20


class RacetrackCreate(CreateView):
    model = Racetrack
    form_class = RacetrackForm
    success_url = reverse_lazy('racetracks:list')


class RacetrackDetail(DetailView):
    model = Racetrack


class RacetrackUpdate(UpdateView):
    model = Racetrack
    form_class = RacetrackForm
    success_url = reverse_lazy('racetracks:list')


class RacetrackDelete(DeleteView):
    model = Racetrack
    success_url = reverse_lazy('racetracks:list')
