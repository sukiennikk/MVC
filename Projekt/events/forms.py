from django import forms
from django.forms import inlineformset_factory
from .models import Event, Guest

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz nazwę imprezy...'}),
            'date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
        }

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'is_confirmed']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię i nazwisko gościa...'}),
            'is_confirmed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

GuestFormSet = inlineformset_factory(
    Event, Guest, 
    form=GuestForm, 
    extra=3, 
    can_delete=True
)