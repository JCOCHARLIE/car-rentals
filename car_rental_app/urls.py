"""JCOProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .import views
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from system.views import admin_car_list, admin_msg, order_list, car_created, order_update, order_delete, msg_delete
from accounts.views import (login_view, register_view, logout_view)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    url(r'^$', admin_car_list, name='adminIndex'),
    url(r'^listOrder/$', order_list, name = "order_list"),
    url(r'^(?P<id>\d+)/editOrder/$', order_update, name = "order_edit"),
    url(r'^(?P<id>\d+)/deleteOrder/$', order_delete, name = "order_delete"),
    url(r'^create/$', car_created, name = "car_create"),
    url(r'^message/$', admin_msg, name='message'),
    url(r'^(?P<id>\d+)/deletemsg/$', msg_delete, name = "msg_delete"),
    url(r'^car/', include('system.urls')),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
