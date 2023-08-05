from django.forms import ModelForm
# from django.contrib.auth.models import User

from base.models import Notes, User


class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

