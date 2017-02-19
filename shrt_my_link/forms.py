from django import forms
from shrt_my_link.models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url', 'count')
