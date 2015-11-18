from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.QuestionsList.as_view(), name='q-list'),
    url(r'^(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='q-detail'),
]
