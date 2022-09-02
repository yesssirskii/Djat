from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Form for user sign up:
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']