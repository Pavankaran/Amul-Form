"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from MyApp import views  # Import views from your app (change MyApp to your app name) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('MyApp.urls')),
    path('appointment_request/', views.create_appointment, name='create_appointment'),
    path('',views.my_view, name='my_view'),

]

handler400 = 'MyApp.views.bad_request'
handler403 = 'MyApp.views.permission_denied'
handler404 = 'MyApp.views.page_not_found'
handler500 = 'MyApp.views.server_error'
