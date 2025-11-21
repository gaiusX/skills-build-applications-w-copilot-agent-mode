from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"profiles", views.UserProfileViewSet)
router.register(r"activities", views.ActivityViewSet)
router.register(r"teams", views.TeamViewSet)
router.register(r"leaderboard", views.LeaderboardEntryViewSet)
router.register(r"suggestions", views.WorkoutSuggestionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
