from django.urls import path
from .views import home,contact,about,resume,service
urlpatterns = [
    path('',home,name='index'),
    path('Contact-Us',contact,name='contact'),
    path('About',about,name='about'),
    path('Resume',resume,name='resume'),
    path('Service',service,name='service')
]