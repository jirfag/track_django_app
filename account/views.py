from django.views.generic.edit import FormView
from django.conf import settings
from .forms import UserCreationForm

class RegistrationView(FormView):
    template_name = 'account/register.html'
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
