# PaisaWala
A budget app which keep the notes of the daily-expenses for different users. It has following features:
1. Registeration and login/logout feature provided.
2. User can store their regular expense.
3. Latest 5 expenses will be displayed.
4. Admin can the control the time for the periodical reset of the total expenditure for its users.
5. Link for the site changes according to the username.

# Requirements:
Django version 3.0.4

Celery version 4.4.4

# How to Set Up in System:
1. Clone the repository into your system.

```
 git clone the repository
```

2. Migrate the files.

``` 
python manage.py migrate
``` 

3. Create the superuser (admin section) and provided the password and email for it.

``` 
python manage.py createsuperuser
```
4. Run the server.
```
python manege.py runserver
```
5. Proceed to signup page.
```
localhost:8000/signup
```
