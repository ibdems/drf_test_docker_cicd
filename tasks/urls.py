from rest_framework import routers

from .views import CategoryViewSet, TaskViewSet

app_name = "tasks"

router = routers.SimpleRouter()
router.register("tasks", TaskViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = router.urls
