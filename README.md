
# rosha_application

This is project about creating application. And after that, a form will be created automatically for the referee responsible for scoring the performance.

  

This project is using python langauge and django framework for the backend. django template and tailwindcss for the frontend. sqlite for database.

  

---

  

## Installtion

- Create pip environment for this project. This project. .gitignore file has been created by this project and specified environment folder to be ignored.

```
python -m venv { name of env.}
```

- Activate environment.

```
{ name of env.}\Scripts\activate
```

- Install all packages pip with and requirements.txt

```
pip install -r requirements.txt
```

- Migrate to create db.

```
python manage.py migrate
```

- Create superuser

```
python manage.py createsuperuser
```
- install tailwindcss

   
```
 npm install -D tailwindcss
```
 - Run tailwindcss build process
```
npm run build
```
 - Run server

```
python manage.py runserver
```


- Normally, if we install django, we will already have sqlite as default database. But I recommend installing sqlite to be able to use sql command line, it will make us work more efficiently. Link for installing sqlite [https://www.sqlitetutorial.net/download-install-sqlite/](https://www.sqlitetutorial.net/download-install-sqlite/)

- There is a chance that there may be a problem installing django-versatileimagefield package. Follow the instructions that are specified in the manual.

https://django-versatileimagefield.readthedocs.io/en/latest/installation.html

- The first time we create superuser. We haven't set the is_judge property yet. We have to go to admin panel to configure is_judge to be True, To be able to access all the functionality that an administrator should be able to. (Later it will be changed to default for superuser and staff.)

---

## Project Detail

  

**Users have been defined as follows.**

-  **is_active** for general users.

-  **is_judge** for users who can set scores.

-  **is_staff** for staff user.

-  **is_superuser** for admin.

---

**Model**

Now, we have 4 models in project.

  

-  **CustomUser Model**

-  **Competition Model** for creating competition detail.

-  **Auditioner Model** for applicant. This model will have another two models connected as follows.

1. "user" field connected in ForeignKey with CustomUser model.

2. "competition" field connected in ForeignKey with Competition model.

-  **Score Model** for referee to fill-in score.

1. "auditioner" field connected in OneToOneField with Auditioner model.

---
