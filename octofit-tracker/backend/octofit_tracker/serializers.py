from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("id", "user", "display_name", "bio")


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ("id", "user", "activity_type", "duration_minutes", "distance_km", "timestamp")


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name", "members")


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = ("id", "user", "score", "date")


class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = ("id", "title", "description", "recommended_for")
