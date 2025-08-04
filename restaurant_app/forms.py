from django import forms
from .models import Reservation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
