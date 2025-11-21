from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data first
        WorkoutSuggestion.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.filter(username__startswith='hero_').delete()

        # Marvel team
        marvel_heroes = [
            {"username": "hero_ironman", "email": "ironman@marvel.com", "display_name": "Iron Man"},
            {"username": "hero_captain", "email": "captain@marvel.com", "display_name": "Captain America"},
            {"username": "hero_blackwidow", "email": "blackwidow@marvel.com", "display_name": "Black Widow"},
        ]
        marvel_profiles = []
        for hero in marvel_heroes:
            user = User.objects.create(username=hero["username"], email=hero["email"])
            user.set_password("password")
            user.save()
            profile = UserProfile.objects.create(user=user, display_name=hero["display_name"], bio="Marvel superhero")
            marvel_profiles.append(profile)

        marvel_team = Team.objects.create(name="Marvel")
        marvel_team.members.set(marvel_profiles)

        # DC team
        dc_heroes = [
            {"username": "hero_batman", "email": "batman@dc.com", "display_name": "Batman"},
            {"username": "hero_superman", "email": "superman@dc.com", "display_name": "Superman"},
            {"username": "hero_wonderwoman", "email": "wonderwoman@dc.com", "display_name": "Wonder Woman"},
        ]
        dc_profiles = []
        for hero in dc_heroes:
            user = User.objects.create(username=hero["username"], email=hero["email"])
            user.set_password("password")
            user.save()
            profile = UserProfile.objects.create(user=user, display_name=hero["display_name"], bio="DC superhero")
            dc_profiles.append(profile)

        dc_team = Team.objects.create(name="DC")
        dc_team.members.set(dc_profiles)

        # Activities, leaderboard, suggestions
        for profile in marvel_profiles + dc_profiles:
            Activity.objects.create(user=profile, activity_type="run", duration_minutes=30, distance_km=5.0)
            LeaderboardEntry.objects.create(user=profile, score=100.0)
            WorkoutSuggestion.objects.create(title=f"Workout for {profile.display_name}", description="Superhero workout.", recommended_for=profile)

        self.stdout.write(self.style.SUCCESS("Superhero test data populated for Marvel and DC teams."))