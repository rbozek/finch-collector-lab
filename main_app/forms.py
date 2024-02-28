from django.forms import ModelForm
from .models import Brushing

class BrushingForm(ModelForm):
  class Meta:
    model = Brushing
    fields = ['date', 'brushing']