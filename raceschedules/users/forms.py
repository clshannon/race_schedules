import geocoder
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import User, UserProfile

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    zip = forms.CharField(max_length=5)
    
    class Meta:
        model = UserProfile
    
    def signup(self, request, user):
        user.save()
        
        profile = UserProfile()
        profile.zip = self.cleaned_data['zip']
        profile.user = user
        
        # Save profile info
        profile.save()
  
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]
        
ProfileFormSet = inlineformset_factory(User, UserProfile, extra=1, fields=('street1', 'street2', 'city', 'state', 'zip'),  can_delete=False)