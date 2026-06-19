from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Event, Guest
from .forms import EventForm, GuestForm, GuestFormSet

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    ordering = ['date']

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['guests'] = GuestFormSet(self.request.POST)
        else:
            data['guests'] = GuestFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        guests = context['guests']
        if guests.is_valid():
            self.object = form.save()
            guests.instance = self.object
            guests.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['guests'] = GuestFormSet(self.request.POST, instance=self.object)
        else:
            data['guests'] = GuestFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        guests = context['guests']
        if guests.is_valid():
            self.object = form.save()
            guests.instance = self.object
            guests.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class GuestCreateView(CreateView):
    model = Guest
    form_class = GuestForm
    template_name = 'events/guest_form.html'

    def form_valid(self, form):
        event = get_object_or_404(Event, pk=self.kwargs['event_pk'])
        form.instance.event = event
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.kwargs['event_pk']})

def toggle_guest_status(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    guest.is_confirmed = not guest.is_confirmed
    guest.save()
    return redirect('event_detail', pk=guest.event.pk)