"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import IndexView, TaskCreateView, DeleteView, TaskView, UpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('tasks/add/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('tasks/<int:pk>/delete/', DeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update/', UpdateView.as_view(), name='task_update')
]
