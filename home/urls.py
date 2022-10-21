from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Lets Explore Tours Admin"
admin.site.index_title = "Welcome to Lets Explore Tours"
admin.site.site_title = "Lets Explore Tours"

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.aboutus,name='aboutus'),
    path('services', views.services,name='services'),
    path('contact', views.contact,name='contact'),
    path('tours', views.tours,name='tours'),
    path('booknow', views.booknow,name='booknow'),

]
