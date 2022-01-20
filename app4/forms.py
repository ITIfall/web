from .models import Announcement
from django import forms
import datetime


class AnnForm (forms.ModelForm):

    class Meta:
        model = Announcement
        fields = ('nick_name', 'description', 'price', 'rubric')


