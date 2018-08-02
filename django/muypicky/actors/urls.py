from django.conf.urls import url
from django.views.generic import FormView

from . import views

from .views import ActorView
#from .views import EmployeeDetailView

app_name = 'actors'

urlpatterns = [
    url(r'^$', views.act_listview),
    url(r'^create/$', ActorView.as_view(), name='actors'),
    url(r'^create/your-name/$', views.ActorView.as_view(), name='actors'),
    url(r'^create/your-name/thanks/$', views.ActorView.as_view(), name='actors'),
    url(r'^search-form/$', views.act_form),
    url(r'^search/$', views.act_search),
]
