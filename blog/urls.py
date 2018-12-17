from django.urls import  path
from . import views
urlpatterns = [
	 path('', views.index, name='index'),
    path('show/<id>', views.show, name='show'),
    path('contact/', views.contact, name='contact'),
	
]