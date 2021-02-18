# Sistema de controde de acessos

Ferramenta para listar os acessos dos usuários e manter um controle de revisão

## Commands
```
python -m pip install Django
django-admin startproject access_val .
python3 manage.py startapp acessos
python manage.py runserver
```

Usa##ndo Docker-compose

```
docker-compose build
docker-compose run
docker-compose run app bash
python manage.py migrate
python manage.py createsuperuser
```
