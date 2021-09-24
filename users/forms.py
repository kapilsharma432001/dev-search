from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill

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
        fields = ['name', 'username', 'email', 'location', 'email', 'short_intro',
        'bio', 'profile_image', 'social_github', 'social_twitter', 'social_linkedin', 
        'social_youtube']


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input' })
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['username'].widget.attrs.update({'class': 'input'})
        self.fields['location'].widget.attrs.update({'class': 'input'})
        self.fields['short_intro'].widget.attrs.update({'class': 'input'})
        self.fields['bio'].widget.attrs.update({'class': 'input'})
        self.fields['profile_image'].widget.attrs.update({'class': 'input'})
        self.fields['social_github'].widget.attrs.update({'class': 'input'})
        self.fields['social_twitter'].widget.attrs.update({'class': 'input'})
        self.fields['social_linkedin'].widget.attrs.update({'class': 'input'})
        self.fields['social_youtube'].widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'input' })
        self.fields['description'].widget.attrs.update({'class': 'input'})



    
        