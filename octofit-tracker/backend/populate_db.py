import os
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')

import django
from django.core.management import call_command

def run():
    django.setup()
    call_command('populate_test_data')

if __name__ == '__main__':
    run()
