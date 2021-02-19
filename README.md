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
docker run -d \
    --name db_p \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=postgres \
    -p 5432:5432 \
    -v /home/rhuan/git_project/access_val/db:/var/lib/postgresql/data:z \
    postgres