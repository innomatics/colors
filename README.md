# Colors API

Provide API to produce random color swatch data.

## Setup

Requires a python 3.8 environment

```bash
pip install -r requirements.txt
./manage.py migrate
./manage.py test 
./manage.py runserver
```

## Interface

### Generate a new random swatch
GET http://localhost:8000/swatches/new

### View all previously generated swatches
GET http://localhost:8000/swatches/new

## Adding a new color space

Currently, supported color spaces:
- SRGB (reference)
- HSL (alternate)

To implement a new alternate color space:
- create a new class similar to `/swatch/models/color.HSL`
- add an instance of the class as a cached property to `Colors`
- create a new serializer and add to the `SwatchSerializer`