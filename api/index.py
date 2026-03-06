import os
import sys
from pathlib import Path

# Add project root to path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Set Django settings
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "student_management_project.settings"
)

# Initialize Django
import django
django.setup()

# Get the WSGI application
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()