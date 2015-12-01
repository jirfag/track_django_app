from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
import views

urlpatterns = [
    url(r'^login$', auth_views.login, {'template_name': 'account/login.html',}, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),
    url(r'^register$', views.RegistrationView.as_view(), name='register'),
]
