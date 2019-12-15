from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.photo_category,name='photoCategory'),
    url('^travel/$',views.travel,name='travel'),
    url('^school/$',views.school,name='school'),
    url('^party/$',views.party,name='party'),
    url('^hiking/$',views.hiking,name='hiking'),
    url('^nature/$',views.nature,name='nature'),
    url('^family/$',views.family,name='family')
]