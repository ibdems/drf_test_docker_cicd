from django.http import JsonResponse
from rest_framework import mixins, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import TaskFilter
from .models import Category, Task
from .permissions import IsCompletedAdmin, ReadOnly
from .serializers import CategorySerializer, TaskSerializer

# ListAPIView, CeateAPIView, RetrieveAPIView, UpdateAPIView, DestryAPIView


class TaskViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsCompletedAdmin, ReadOnly]
    authentication_classes = [
        JWTAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    ]
    lookup_field = "id"
    pagination_class = LimitOffsetPagination
    filterset_class = TaskFilter
    search_fields = ["name", "description", "category__name"]
    # ordering_fields = ['created_at', 'expired_at', 'level']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


# or ReadOnlyModelViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    pagination_class = None


def custom_404_view(request, exception=None):
    # Si c'est une api
    return JsonResponse(
        {
            "detail": "Page non trouve",
        },
        status=404,
    )

    # Si une vue
    # return render(request, '404.html')


def custom_500_view(request, excetion=None):
    # Si c'est une api
    return JsonResponse(
        {
            "detail": "Une erreur est survenue",
        },
        status=500,
    )

    # Si une vue
    # return render(request, '500.html')
