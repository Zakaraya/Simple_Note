from .views import NoteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = router.urls


