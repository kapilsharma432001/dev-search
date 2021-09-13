from django.db.models.base import Model
from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder':'Add Title'})
        self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder':'Add Description'})
        self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder':'Paste Demo Link'})
        self.fields['source_link'].widget.attrs.update({'class': 'input', 'placeholder':'Paste Source Link'})
        
            