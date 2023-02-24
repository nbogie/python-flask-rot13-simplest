# Simplest python flask app

Including a simple module and unit tests.

### To install

If no venv dir exists:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### To start the app:

(assuming you've already activated the venv with `source venv/bin/activate`)

```
flask run
```

### To run the unit tests:

(assuming you've already activated the venv with `source venv/bin/activate`)

```
python test_rot13.py
```

or

```
python -m unittest
```

### To deploy to production

Follow https://render.com/docs/deploy-flask

The app already mentions the production http server, gunicorn, in `requirements.txt` and doesn't hard-code a port environment variable, allowing render and gunicorn to coordinate that.
