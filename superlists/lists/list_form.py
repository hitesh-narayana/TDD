from django.forms import ModelForm, TextInput

from .models import List

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = "__all__"