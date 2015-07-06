from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.user_login, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^history$', views.user_history, name='history'),
]