# Dbase_connectors
(All in one)...
This package help developers to connect thier projects with different databases including sqlite, sqlserver, mysql, mariadb and postgresql. Developers don't have to search which package must be installed to connect with thier databases. 

## Installation
pip install Dbase-connectors

## Usage
##### sqlite connector
```
from connectors import Connector
connector = Connector()

cursor = connector.sqlite_connect("path/sqlite.db")
cursor.execute("select * from Users")
users = cursor.fetchall()
```

##### sqlserver connector
```
from connectors import Connector
connector = Connector()

cursor = connector.sqlserver_connect(
    driver="ODBC Driver 17 for SQL Server",
    server="server with instance",
    database="database name",
    user="your user",
    password="your password",
    )
    
users = cursor.execute("select * from auth_user").fetchall()
```

##### mysql mariadb connector
```
from connectors import Connector
connector = Connector()

connection = connector.mysql_mariadb_connect("host", "dbname", "user",  "password", port=3306 """default port""" )
cursor = connection.cursor()
cursor.execute("select * from players")
players = cursor.fetchall()
```

##### postgresql
```
from connectors import Connector
connector = Connector()

cursor = connector.postgresql_connect("host", "dbname", "user", "password", port='5432', """default port""")
cursor.execute("select * from users")
users = cursor.fetchall()

```
