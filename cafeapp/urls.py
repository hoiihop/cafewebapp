"""cafeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from report import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', auth_views.login, name='login'),
    path('admin/', admin.site.urls),
    path('report/', views.index, name='index'),
    path('report/create/', views.create_report, name='new_report'),
    path('report/add/', views.add_lines, name='add_lines'),
    path('report/view/<int:id>', views.report_view, name='report_view'),
    path('report/change/<int:id>', views.change_report, name='change_report'),
    path('report/change/q/<int:id>', views.change_lines, name='change_lines'),
    path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),
]
