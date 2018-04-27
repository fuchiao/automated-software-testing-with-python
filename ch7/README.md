# ch7 #

----

this codes are adapted from ch6

we add some new feature

* add userModel and allow users login
* implement resources
* authentication by jwt
* add system tests for resources and authentication

Reference

* https://github.com/trendiguru/falcon-jwt/blob/master/falcon_jwt.py
* https://eshlox.net/2017/07/28/integrate-sqlalchemy-with-falcon-framework/
* http://tech.colla.me/zh/show/token_session_cookie
* http://falcon.readthedocs.io/en/stable/user/quickstart.html
* http://falcon.readthedocs.io/en/stable/api/errors.html

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
