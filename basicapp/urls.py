from django.conf.urls import url
from basicapp import views
app_name='basicapp'
urlpatterns=[
    url(r'^login/',views.user_login,name='user_login'),
    url(r'special/',views.special,name='special'),
    url(r'^logout/',views.user_logout,name='user_logout'),
    url(r'^registration/',views.registeration,name='registration'),
]
