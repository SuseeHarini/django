from django.conf.urls import url
from books import views
from .views import BookView

app_name = 'books'

urlpatterns = [
    url(r'^$', views.book_listview),
    url(r'^create/$', BookView.as_view(), name='book'),
    url(r'^create/your-name/$', views.BookView.as_view(), name='book'),
    url(r'^create/your-name/thanks/$', views.BookView.as_view(), name='book'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
]
