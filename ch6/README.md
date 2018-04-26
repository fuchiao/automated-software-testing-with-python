# ch6 #

----

this codes are adapted from ch5

we add some new feature

* add store model and use foreign key
* add tests for foreign key

sqlite does not support foreign key, so we replace with postgresql

run database service on docker
```
$ docker run -e POSTGRES_PASSWORD=pa55 -d -p 5432:5432 postgres
```
connect service
```
$ psql postgresql://postgres:pa55@127.0.0.1:5432
```
reset tables
```
$ env DB_URI=127.0.0.1  python db.py
```

TODO: create a session for every request and rollback if something fails
https://eshlox.net/2017/07/28/integrate-sqlalchemy-with-falcon-framework/
