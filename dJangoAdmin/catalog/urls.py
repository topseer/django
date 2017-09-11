from django.conf.urls import url

from . import views


# Create your tests here.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
]