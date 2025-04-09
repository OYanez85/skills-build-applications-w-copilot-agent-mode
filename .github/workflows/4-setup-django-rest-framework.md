# Step 4: Verify Django REST Framework and Djongo Configuration

This GitHub Actions step verifies the following:
- Djongo is configured in `settings.py`
- The MongoDB host `localhost:27017` is reachable
- The `rest_framework` and `tracker` apps are listed in `INSTALLED_APPS`

```yaml
name: Verify Django REST Framework and Djongo Configuration

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  verify-django-config:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r octofit-tracker/backend/requirements.txt

      - name: Verify Djongo configuration in settings.py
        run: |
          if ! grep -q '"ENGINE": "djongo"' octofit_tracker/settings.py; then
            echo "Error: Djongo is not configured in settings.py" >&2
            exit 1
          fi

      - name: Verify MongoDB host is reachable
        run: |
          if ! nc -z localhost 27017; then
            echo "Error: MongoDB host localhost:27017 is not reachable" >&2
            exit 1
          fi

      - name: Verify required apps in INSTALLED_APPS
        run: |
          if ! grep -q '"rest_framework"' octofit_tracker/settings.py || ! grep -q '"tracker"' octofit_tracker/settings.py; then
            echo "Error: Required apps are not listed in INSTALLED_APPS" >&2
            exit 1
          fi
```
