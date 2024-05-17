from django.urls import path
from . import views


app_name = 'oauth_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upload_file, name='upload_file'),
    path('submitted/', views.submitted, name='submitted'),
    path('update/<int:pk>/', views.update_file, name='update_file'),
    path('delete_report/<int:pk>/', views.delete_report, name='delete_report'),
    path('delete_admin_report/<int:pk>/', views.delete_admin_report, name='delete_admin_report'),
    path('my_report/<int:pk>/', views.my_report, name='my_report'),
    path('admin_report/<int:pk>/', views.admin_report, name='admin_report'),
]
