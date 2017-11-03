from django.conf.urls import url

from . import views


# Create your tests here.
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    
]



urlpatterns += [   
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]

urlpatterns += [   
    url(r'^dashboard/dateRange/$', views.dashboard, name='dashboard'),
]
