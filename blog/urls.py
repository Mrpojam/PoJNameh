from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_details, name='article_details'),
    path('create-mail/', views.send_mail, name='create_mail')
]

