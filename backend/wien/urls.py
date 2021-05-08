from rest_framework import routers
from .views import PresetViewSet


router = routers.DefaultRouter()
router.register('presets', PresetViewSet)
