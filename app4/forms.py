from .models import Friend
from django import forms
import datetime


class FriendForm (forms.ModelForm):

    class Meta:
        model = Friend
        fields = ('nick_name', 'description', 'price', 'rubric')


