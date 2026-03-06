import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "student_management_project.settings"
)

import django
django.setup()

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()