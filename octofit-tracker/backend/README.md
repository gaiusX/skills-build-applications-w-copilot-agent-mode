OctoFit Tracker backend

This folder contains the backend for the OctoFit Tracker project.

Setup (local):

1. Create virtual environment:

   python3 -m venv octofit-tracker/backend/venv

2. Activate and install requirements:

   source octofit-tracker/backend/venv/bin/activate
   pip install -r octofit-tracker/backend/requirements.txt

Ports used:
- 8000: public (Django dev server)
- 27017: private (MongoDB, if used)
