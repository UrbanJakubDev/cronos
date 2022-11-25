from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
   path('home/', views.index, {}),
   path('report/', views.get_report, {}),
   
    path('', include(router.urls))

]