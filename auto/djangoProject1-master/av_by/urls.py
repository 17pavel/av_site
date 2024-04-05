from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/city', CityViewSet, 'city')
router.register('api/car', CarViewSet, 'car')
router.register('api/user', UserViewSet, 'user')


urlpatterns = router.urls