import sys
from pymongo import MongoClient
from octofit_tracker import settings

try:
    # Extract MongoDB connection details from settings
    db_settings = settings.DATABASES['default']
    host = db_settings.get('HOST', 'localhost')
    port = db_settings.get('PORT', 27017)

    # Attempt to connect to MongoDB
    client = MongoClient(host, port)
    client.server_info()  # Trigger exception if MongoDB is not reachable
    print("MongoDB connection successful")
except Exception as e:
    print(f"MongoDB connection failed: {e}", file=sys.stderr)
    sys.exit(1)
