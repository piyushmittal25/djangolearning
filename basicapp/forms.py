from django import forms
from basicapp.models import UserProfileInfo
from django.contrib.auth.models import User
class userinfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileInfoform(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('portfolio','profilepicture')
