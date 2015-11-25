from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', views.QuestionsList.as_view(), name='q-list'),
    url(r'^(?P<pk>\d+)/$', cache_page(1)(views.QuestionDetail.as_view()), name='q-detail'),
]
