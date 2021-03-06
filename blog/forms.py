from django.forms import ModelForm
from blog.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('name', 'description',)
