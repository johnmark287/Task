from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterUsetView, LoginView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUsetView.as_view(), name='regiser'),
    path('login/', LoginView.as_view(), name='login'),
]