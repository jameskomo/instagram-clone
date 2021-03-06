from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('home/', views.home, name='my_instagram-home'),
    path('profile/', views.home, name='my_instagram-profile'),
    path('new_post/', views.new_post, name='my_instagram-new-post'),
    url(r'^search/', views.search_image, name='images-search'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)