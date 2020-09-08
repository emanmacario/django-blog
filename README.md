# HackerJourney
A blogging website written in Python 3 and Django 3.1 to document my own personal coding and learning journey in the future.

## Motivation
The motivation for creating this project was to learn Django web development, to improve my HTML/CSS skills, and to learn a bit about the deployment of Python web servers.

## Deployment on Heroku
Ensure you have the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed

1. Install `django-heroku`
    ```bash
    $ pip install django-heroku
    ```

2. Activate `django-heroku` in your `settings.py` file. This will automatically read the `DATABASE_URL` variable for your PostgreSQL database
    ```python
    # Activate django-heroku
    import django_heroku
    django_heroku.settings(locals())
    ```

2. Run migrations
    ```bash
    $ heroku run python manage.py migrate
    ```

3. Create a superuser for the Django admin app
    ```bash
    $ heroku run bash
    $ python manage.py createsuperuser
    ```
