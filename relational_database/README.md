# PLAN OF THE LECTION

# RDBMS

# SQL basic commands

# Integration with python

### PyCharm configuration

### Migration

### Fixtures

### Tests

# Useful information

How to configure your Postgres environment

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

Same information for those one who does not like English (yet) 

https://timeweb.com/ru/community/articles/kak-ustanovit-postgresql-na-ubuntu-18-04-1 

Links for windows

https://www.w3resource.com/PostgreSQL/connect-to-postgresql-database.php

> - sudo -u postgres psql
> - postgres=# create database cursor_db;
> - postgres=# create user cursor with encrypted password 'very_secret_password';
> - postgres=# grant all privileges on database cursor_db to cursor;
> - postgres=# ALTER USER cursor WITH SUPERUSER;
> - postgres=# \q;
  

From linux shell
    psql -h localhost -U cursor -d cursor_db -p 5433 ( or 5432 based on your version of OS)


If you catch this error installing psycopg2 in your virtual env
```
    Error: b'You need to install postgresql-server-dev-X.Y for building a server-side extension or libpq-dev for building a client-side application.\n'
``` 

Running next commands could fix your problem 

```
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
sudo apt-get install python3.7-dev

```


 When you are in psql command line type
```.postgres=# 

\help
\?

```
to see all possible commands

About basic commands in psql you could read here 
http://www.postgresqltutorial.com/psql-commands/


If you could connect to database with this command
```
psql -h localhost -d cursor_db -U cursor -p 5433

```

But still could not connect with python code 
```
subl /etc/postgresql/9.6/main/pg_hba.conf
```
Your version of psql could be another, look in dir /etc/postgresql/

and change `local all all peer` to `local all all password`

Then you need to restart your postgres service

```.env
sudo service postgresql restart
```

If you still have problems with installing pyscopg2

try to do next

```
ls -la /usr/lib/postgresql/
# look on version of postgress

export PATH=/usr/lib/postgresql/your_version_here/bin/:$PATH

```


```.env
sudo apt install build-essential
```