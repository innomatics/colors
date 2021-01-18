# Colors API

Provide API to produce random color swatch data.

## Setup

Requires a python 3.8 environment

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Interface

### Generate a new random swatch
GET http://localhost:8000/swatches/new

### View all previouslt generated swatches
GET http://localhost:8000/swatches/new
