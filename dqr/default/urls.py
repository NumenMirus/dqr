from django.urls import path
from default import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addqrcode', views.addqrcode, name='addqrcode'),
    path('deleteqrcode', views.deleteqrcode, name='deleteqrcode'),
]
