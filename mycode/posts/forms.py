from django import forms
from .models import post
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class postform(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(attrs={
            'required': False,
            'cols': 30,
            'rows': 10
        }))

    class Meta:
        model = post
        fields = [
            'title',
            'content',
            'image',
            'draft',
        ]
