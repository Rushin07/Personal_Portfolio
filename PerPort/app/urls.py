from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.handleblog, name='handleblog'),
    path('resume', views.resume, name='resume'),

    
]
