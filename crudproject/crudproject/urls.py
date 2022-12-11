"""crudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('account/', views.add_show,name='Account_add'),
    path('add/', views.add_show_contact,name='Contact_add'),
    path('list/',views.account_list,name='list'),
    path('Clist/',views.contact_list,name='Clist'),
    path('deletedata/<int:id>/',views.account_delete,name='delete'),
    path('Aupdate/<int:id>/',views.update_account,name='Aupdate'),
    path('Cdelete/<int:id>/',views.contact_delete,name='Cdelete'),
    path('Cupdate/<int:id>/',views.update_contact,name='Cupdate'),
]
