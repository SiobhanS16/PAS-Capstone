import os

def getSecrets():
    secrets = {
        'MONGO_HOST':os.environ.get('pas_mongodb_host'),
        'MONGO_DB_NAME':'pasdb',
        'GOOGLE_CLIENT_ID': os.environ.get('pas_google_client_id'),
        'GOOGLE_CLIENT_SECRET':os.environ.get('pas_google_client_secret'),
        'GOOGLE_DISCOVERY_URL':"https://accounts.google.com/.well-known/openid-configuration"
        }
    return secrets