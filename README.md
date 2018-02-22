# Todo-list
Extremely simple todo list project on Python,Django and Bootstrap 4

# Features (now)
## Integrating Google and GitHub Sign-In
![1](https://github.com/VladislavShipovskoi/django-todo-list/blob/master/screenshots/login.png)

## Add/Edit/Delete tasks
![2](https://github.com/VladislavShipovskoi/django-todo-list/blob/master/screenshots/main.png)
## Viewing completed tasks
![3](https://github.com/VladislavShipovskoi/django-todo-list/blob/master/screenshots/completed.png)

# Start
* install packages (```pip install -r requirements.txt```)
* migrate (```python manage.py migrate```)
* create superuser (```python manage.py createsuperuser```)
* get the google and github oauth pair (key/secret)
* Open settings.py and set the variables corresponding to the
  * **SOCIAL_AUTH_GOOGLE_OAUTH2_KEY**
  * **SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET**
  * **SOCIAL_AUTH_GITHUB_KEY**
  * **SOCIAL_AUTH_GITHUB_SECRET**
* run project (```python manage.py runserver```)
* go to **http://localhost:8000**
