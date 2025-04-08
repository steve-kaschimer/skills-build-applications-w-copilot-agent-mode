# Rename the project and app references to 'octofit-tracker'
INSTALLED_APPS = [
    # ...existing apps...
    'fitness',
    'octofit-tracker.backend.octofit_tracker',
]

# Update the database configuration for the 'octofit-tracker' app
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_tracker_db',
    }
}

# Update CORS headers configuration for the 'octofit-tracker' app
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Frontend URL
]