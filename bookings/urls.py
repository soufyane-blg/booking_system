from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.booking_list, name='booking_list'),
    path('create/', views.booking_create, name='booking_create'),
    path('<int:id>/details/', views.booking_details, name='booking_details'),
    path('<int:id>/update/', views.booking_update, name= 'booking_update'),
    path('<int:id>/delete/', views.booking_delete, name = 'booking_delete'),
    path('test/', views.test),

]

