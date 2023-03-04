from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *
from .routes import *
from .auth import *
from .annotation import *

urlpatterns = [
    # routes 
    path('', loginpage),
    path('login', loginpage),
    path('signup',signup),
    path('home', home),
    # path('annotate_page',annotate_page),
    path('annotation',annotation),
    path('annotate_page/<str:p_name>',annotate_page),
    path('layout',layout),



    # APIS
    path('newuser',newuser),
    path('signin',signin),
    path('project_details',project_details),
    path('add_users',users),
    path('get_images',get_images),
    path('start_magic',start_magic),
    path('assign_user',assign_user),

    path('create_project',create_project),

    ]+ static(settings.STATIC_URL, document_root='./static/', )


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
