# Todo-list
Extremely simple todo list project on Python,Django and Bootstrap 4

# Features (now)
## Integrating Google and GitHub Sign-In
![1](https://user-images.githubusercontent.com/17500704/38317777-0f4ed3e0-3858-11e8-85ac-48a1c5a234cb.png)

## Add/Edit/Delete tasks
![2](https://user-images.githubusercontent.com/17500704/38317839-298c85d6-3858-11e8-8531-9ab4b1df71c1.png)
## Viewing completed tasks
![3](https://user-images.githubusercontent.com/17500704/38317880-46df49fc-3858-11e8-91cc-1b78b1e0ec59.png)

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
