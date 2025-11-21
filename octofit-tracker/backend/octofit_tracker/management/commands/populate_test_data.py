from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from octofit_tracker.models import UserProfile, Activity, Team, LeaderboardEntry, WorkoutSuggestion


class Command(BaseCommand):
    help = "Populate octofit_db with test data for OctoFit Tracker"

    def handle(self, *args, **options):
        self.stdout.write("Creating test users...")
        users = []
        for i in range(1, 4):
            username = f"testuser{i}"
            user, created = User.objects.get_or_create(username=username, defaults={"email": f"{username}@example.com"})
            if created:
                user.set_password("password")
                user.save()
            profile, _ = UserProfile.objects.get_or_create(user=user, defaults={"display_name": f"Tester {i}", "bio": "Test user"})
            users.append(profile)

        self.stdout.write("Creating teams...")
        team, _ = Team.objects.get_or_create(name="Alpha Team")
        team.members.set(users[:2])
        team.save()

        self.stdout.write("Creating activities and leaderboard entries...")
        for idx, profile in enumerate(users, start=1):
            Activity.objects.create(user=profile, activity_type="run", duration_minutes=30 * idx, distance_km=5.0 * idx)
            LeaderboardEntry.objects.create(user=profile, score=100.0 * idx)
            WorkoutSuggestion.objects.create(title=f"Workout for {profile}", description="A balanced workout.", recommended_for=profile)

        self.stdout.write(self.style.SUCCESS("Test data population complete."))
