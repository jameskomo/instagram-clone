from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('', views.home, name='my_instagram-home'),
    path('profile/', views.profile, name='my_instagram-profile'),
    url(r'^search/', views.search, name='my_instagram-search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)