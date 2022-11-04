"""ihaKiralamaPlatformu URL Configuration

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
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from system.views import admin_iha_list, admin_msg, order_list, iha_created, order_update, order_delete, msg_delete
from ihaKiralama.views import (login_view, register_view, logout_view)

#URL adresleri, evrensellik teşkil etmesi için İngilizce bırakıldı
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', admin_iha_list, name='adminIndex'),
    re_path(r'^listOrder/$', order_list, name = "order_list"),
    re_path(r'^(?P<id>\d+)/editOrder/$', order_update, name = "order_edit"),
    re_path(r'^(?P<id>\d+)/deleteOrder/$', order_delete, name = "order_delete"),
    re_path(r'^create/$', iha_created, name = "iha_create"),
    re_path(r'^message/$', admin_msg, name='message'),
    re_path(r'^(?P<id>\d+)/deletemsg/$', msg_delete, name = "msg_delete"),
    re_path(r'^iha/', include('system.urls')),
    re_path(r'^login/', login_view, name='login'),
    re_path(r'^logout/', logout_view, name='logout'),
    re_path(r'^register/', register_view, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)