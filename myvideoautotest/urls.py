"""myvideoautotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from documentapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^listone/$', views.listone),
	url(r'^listall/$', views.listall),
    url(r'^$', views.index),
    url(r'^index/$', views.index),

    #CRUD
	url(r'^post/$', views.post), #資料新增，資料作驗證
    url(r'^delete/(\d+)/$', views.delete), #刪除
	url(r'^edit/(\d+)/(\w+)$', views.edit), #編輯
    url(r'^postform/$', views.postform), # 表單驗證

    #會員系統
    # url(r'^adduser/$', views.adduser)
    url(r'^adduser/(\w+)/(\w+)/(\w+)/(\w+)$', views.addUser),

    url(r'^detail/(\d+)/$', views.detail),
]
