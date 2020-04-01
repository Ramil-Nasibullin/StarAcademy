from django.forms import ModelForm, Form
from . import models
from django import forms
from .models import RecrutRegistrationForm
from django.http import HttpResponse


class CreateNewRecrut(ModelForm):
    class Meta:
        model = RecrutRegistrationForm
        fields = ['name', 'planet', 'age', 'mail']








