# E-Commerce-Website-Using-Python


## Summary

Hello friends, This is my first full e-commerce project with Python-Flask. This is free. Anybody can use and moderate this project.

## Platform Used

### Front-End

(i) HTML5 <br>
(ii) CSS3 <br>
(iii) JavaScript <br>
(iv) Bootstrap <br>

### Back-End

(i) Python - Flask <br>
(ii) MySQL <br>

## Key Features

### Public User

(i) Search Product <br>
(ii) View Product <br>
(iii) Create User Account <br>

### Signin User

(i) Search Product <br>
(ii) View Product <br>
(iii) Create Order <br>
(iv) Change Email & Password <br>
(v) Can View Previous Order with UPDATE and DELETE <br>

### Admin

(i) Add New Product <br>
(ii) Update Product <br>
(iii) See all Orders <br>
(iv) Manage all Users <br>

## Conclusion

There are also many more feature which are not in the list. Feel free to use this project
# start project

```set up your db config in app.py fom line21```
```app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'system'
app.config['MYSQL_DB'] = 'menshut'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
```
```
python -m venv venv
```

```
.\venv\Scripts\Activate
```

```
pip install -r requirements.txt
pip install -r requirements_full.txt
```

If you see an error like:

```

ModuleNotFoundError: No module named 'flask_sqlalchemy'
```

Just install it manually:

```python
pip install flask_sqlalchemy
```

Then update your requirements.txt with:

```
pip freeze > requirements.txt
```

-for exit from env
```
deactivate
```

 > credentials
username: admin@gmail.com   
pass: admin@123
to customise admin pass change the hash by runnig the file=> databse> adminpassgen.py [you can change the password inside the file] its goan generate a hash in the terminal copy and 
 update the admin password hash in the database 
>
> ``` databse basic comands ```

```
select * from menshut.admin;


-- truncate menshut.admin; -- (truncate) will remove all the data from the table by keeping the structure


INSERT INTO `admin` (`id`, `firstName`, `lastName`, `email`, `mobile`, `address`, `password`, `type`, `confirmCode`) VALUES
(1, 'admin', 'admin', 'admin@gmail.com', '123456789012', 'mngr', '$5$rounds=535000$kIwCD6PE4OccMADl$yYrUQQRjguSNoqjJk3846VlrT0vRJk1.3n1l4Tf7S.1', 'manager', '0');

select * from menshut.users; 

-- truncate menshut.users; 

select * from menshut.product_level; 
select * from menshut.product_view; 
select * from menshut.products;

update menshut.admin set firstName="Admin Bro" where id=1;

```

#use mysql workbench or php myadmin

