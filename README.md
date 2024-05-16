# Backend flask app using sqlite.

Once the repo is cloned, run the following commands in the terminal:

```
pipenv install
pipenv shell
```

After installing packages, to use flask session object for cookies, do the following:

1. Create a .env file
2. Create a variable enviroment and set it equal to anything you want. 
3. In the following line add the variable name like so(leave the quotes):

```
app.secret_key= os.getenv('YOUR ENVIROMENT VARIABLE GOES HERE')
```


To initalize the sqlite database, run the following commands in the ubuntu terminal:

```
flask db init
flask db migrate -m 'initial migration with user model'
flask db upgrade
```

To seed the database, run the following command:

```
python seed.py
```