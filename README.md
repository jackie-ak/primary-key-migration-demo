# One does not simply migrate a primary key
> This is the demo app for a talk at the PyCon Austria 2025.
> The slides for the talk are here: https://tantemalkah.at/2025/pycon

To run this app you need docker to run the Postgres database, as well
as the python packages listed in requirements.txt. This is tested with
a Python 3.12 virtual environment created with
[uv](https://docs.astral.sh/uv/).

Once your environment is up, install the requirements, e.g. with
(if you use a classical venv and pip just leave out the `uv`):
```bash
uv pip sync src/requirements.txt
```

You then need to copy the env-skel file to .env, and adapt it accordingly:

```bash
cp env-skel .env
vi .env   # or use nano, or some other text editor
```

> you don't actually need to change anything if you run it once
> locally and throw it away again, but i strongly recommend setting
> a long random database password

Now you are theoretically ready to run the app. But for it to really work, you need
to spin up the database, run the initial migrations, and probably you also want
to set up some demo data. And THEN start the dev server. All of that is done with
the following commands:

```bash
docker compose up -d
cd src
python manage.py migrate
python manage.py loaddata artworks/fixtures/demo_data.json
python manage.py manage.py changepassword demo
python manage.py runserver
```

Now you can visit the demo app on http://127.0.0.1:8000/

The admin interface is at http://127.0.0.1:8000/admin/
