from django.urls import path
from default import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addqrcode', views.addqrcode, name='addqrcode'),
    path('deleteqrcode', views.deleteqrcode, name='deleteqrcode'),
    path('redirect/<str:internal_url>', views.redirect_to_external_url, name='redirect_to_external_url'),
    path('modifyqrcode', views.modifyqrcode, name='modifyqrcode'),
]
