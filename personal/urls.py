from django.conf.urls import url, include
from . import views

# Create your views here.

urlpatterns = [

	url(r'^$',views.index, name='index'),
	url(r'^contact/', views.contact, name='contact'),
]