from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'input' })
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['username'].widget.attrs.update({'class': 'input'})
        self.fields['password1'].widget.attrs.update({'class': 'input'})
        self.fields['password2'].widget.attrs.update({'class': 'input'})
            
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"