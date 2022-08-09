from django.urls import path

from . import views

app_name = 'builders'
urlpatterns = [
    path('city', views.CityList.as_view(), name='city'),
    path('region', views.RegionList.as_view(), name='region'),
    path('country', views.CountryList.as_view(), name='country'),
    path('user', views.UserList.as_view(), name='user'),
    path('syslang', views.Languages.as_view(), name='system-languages'),
]