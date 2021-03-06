from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users',views.userviewset)
router.register(r'groups',views.gruopviewset)

urlpatterns = [
    path('default/',include(router.urls)),
    path('',include('rest_framework.urls',namespace='rest_framework'))
]
