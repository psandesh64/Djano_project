from django.urls import path
from orm_app import views
from .views import upload_csv,download_csv,handletodo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',upload_csv, name='home'),
    path('download/<int:model_id>/', download_csv, name='download_csv'),
    path('api/',views.homeapipage,name='homeapi'),
    path('signup',views.handleSignup,name='signup'),
    path('login',views.handleLogin,name='login'),
    path('logout',views.handleLogout,name='logout'),
    path('picpage',views.image_page,name='picpage'),
    path('picdelpage',views.image_del_page,name='picdelpage'),
    path('todopage',views.handletodo,name='todopage'),
    path('todoedit/<str:id>/',views.handletodoedit,name='todoedit'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)