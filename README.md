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

## Stopping & cleaning up

While the Django dev server (the thing started with the last `runserver`) command
is running, you can hit Ctrl + C to quit. In order to clean up the container, go
up to the root directory again and use docker compose to stop and remove the
containers:

```bash
cd ..
docker compose down
```

Next time to start up everything you can just do:

```bash
docker compose up -d
cd src
python manage.py runserver
```

If you want to start with a fresh database, you need to remove the `postgres`
folder inside the `dockerdata` folder (when the container is currently not
running). And then you need the whole startup sequence from the section before,
including the `migrate`, `loaddata`, and `changepassword` commands.

## How to set up a virtual environment

If you are already using a plain Python installation, the quickest way to set
up a new virtual environment is with:

```bash
python -m virtualenv .venv
```

Then you can start the virtual environment with:

```bash
# On Linux and MacOS
source .venv/bin/activate

# On Windows
.venv\Scripts\activate.bat
```

If you want to get out of your virtual environment without just closing your
terminal window, you can use the `deactivate` command.

Generally I can recommend using [uv](https://docs.astral.sh/uv/) for
handling python versions as well as virtual environments. Once it is
set up properly (which is not very complicated), it provides convenient
and fast ways to install different python versions and set up virtual
environments. And the `uv pip` commands are just soooo much faster
than the classical `pip` commands.