from django.conf.urls import url
from first_app import views

app_name = "first_app"

urlpatterns = [
    url(r'^forms/', views.form_names, name='form_names'),
    url(r'^users/', views.users, name='users'),
    url(r'^other/', views.other, name='other'),
    url(r'^$', views.index, name='index'),
]