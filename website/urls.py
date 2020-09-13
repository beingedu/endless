from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name="home"),
    path('homes/', views.homes, name="homes"),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('project/', views.project, name='project'),
    path('team/', views.team, name='team'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('pricing/', views.pricing, name='pricing'),
]