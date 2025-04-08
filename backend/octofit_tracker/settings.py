# Add MongoDB database connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

# Enable CORS for all origins, methods, and headers
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = ['*']

# Allow all hosts
ALLOWED_HOSTS = ['*']