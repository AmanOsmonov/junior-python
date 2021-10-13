from .models import UserRequest
from django.forms import ModelForm

class RqForm(ModelForm):
    class Meta:
        model=UserRequest
        fields=['link']
