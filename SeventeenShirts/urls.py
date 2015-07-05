from django.conf.urls import include, url
from django.contrib import admin



urlpatterns = [
    url(r'', include('shop.urls', namespace='shop')),
    url(r'^register/', include('accounts.urls', namespace='register')),
    url(r'^admin/', include(admin.site.urls)),
]
