from django.forms import ModelForm
from .models import Nest
from django.contrib.auth.models import User

class NestForm(ModelForm):
    class Meta:
        model = Nest
        fields = '__all__'
        exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']