# django-fullstack-backend

To get fake data for testing run
```bash
python3 test_data/generate.py

# then do these commands, they must be in order (atleast do events last, as it has foreign keys for the other models)
python3 manage.py test_data/artists.json
python3 manage.py test_data/venues.json
python3 manage.py test_data/events.json

# Then run your server
python3 manage.py runserver
```