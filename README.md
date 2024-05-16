Backend flask application using sqlite.

After installing packages, to use flask session object for cookies, do the following:

1. Create a .env file
2. Create a variable enviroment and set it equal to anything you want. 
3. In the following line add the variable name like so:

```
app.secret_key= os.getenv('YOUR ENVIROMENT VARIABLE GOES HERE')
```