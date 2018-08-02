from django.conf.urls import url
from django.views.generic import FormView

from . import views

from .views import EmployeeView
#from .views import EmployeeDetailView

app_name = 'employee'

urlpatterns = [
    url(r'^$', views.emp_listview),
    url(r'^create/$', EmployeeView.as_view(), name='employee'),
    url(r'^create/your-name/$', views.EmployeeView.as_view(), name='employee'),
    url(r'^create/your-name/thanks/$', views.EmployeeView.as_view(), name='employee'),
    url(r'^search-form/$', views.emp_form),
    url(r'^search/$', views.emp_search),
    #url(r'^search/$', views.EmployeeDetailView.as_view(), name='emp'),
]
