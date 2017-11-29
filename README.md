# Database Wrapper
> Boilerplate to manipulate SQL database with python, very easy and simply. Regardless of actual syntax of SQL. It does taylor the sql statement for you in way of OOPS.

- In order to insert data into the database, only you need to be done is
```
DB('example.db').table('users').insert({
	'name': 'Jhon Doe',
	'email': 'doe@domain.com',
	'password': '123456',
})
```
And for multiple records
```
DB('example.db').table('users').insert_many([
	('Jhon Doe', 'doe@domain.com', '12345'),
	('Alexender', 'alexender@domain.com', '12345545'),
])
```
where your database name is ***example.db*** and the table name is ***users***
## Note* sql file for table should be provided in the same directory

Now, to retrive data from database with name filtering
```
DB('example.db').table('users').where('name', 'Jhon Doe').get()
```
It is equivalent to "SELECT * FROM users WHERE name = 'Jhon Doe'"

- To retrive all the records
```
DB('example.db').table('users').all()
```
Which is equivalent to "SELECT * FROM users"

Well this version of Database wrapper isn't compatible to prevent **sql injection**
But still it works ideally. The sql injection prevented version will be available
soon.

- First result for fetch query would be
```
DB('example.db').table('users').where('name', 'Jhon Doe').first()
```
- To retrive certain amount of records then
```
DB('example.db').table('users').where('name', 'Jhon Doe').many(6)
```
will gives you the top 6 records if available.

- To get numbers rows exists in the table
```
DB('example.db').table('users').where('name', 'Jhon Doe').count()
```

It is limited to execute queries, but still there is a method called query
to execute custom queries.
```
db = DB('example.db').query("SELECT * FROM users WHERE email='admin@someone.com' AND password='sdeu8j'")
```
Which will returns the cursor and connection,
you can access them by follwing (db from above statement)
```
db.cur
db.conn
```
