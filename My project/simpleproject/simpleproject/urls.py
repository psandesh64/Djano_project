"""simpleproject URL Configuration

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
from django.urls import path
from simpleapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Homepage,name='home'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('info/<str:pk>/',views.Profile_overview,name='info'),
    path('picpage/<str:pk>/',views.Picturespage,name='picpage'),
    path('picpagedel/<str:pk>/',views.Picturespagedelete,name='picpagedel'),
    path('infoedit/<str:pk>/',views.Infoedit,name='infoedit'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
