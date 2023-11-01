
# URLShortener

A simple URL shortener based on Django framework and MySQL for ITW2 course assignment.

## Features
`Done for the assignment`
- [x] Generate a unique 8 digit token for each URL
- [x] If a URL already has a short URL generated, then display that to user
- [x] Display a table containing all short URLs and corresponding original URLs

`For future *fun* purposes`
- [ ] Add functionality for custom token, if it is available
- [ ] Improve UI?
- [ ] Bash script to automate install process
## Steps to reproduce
This has been tested on Ubuntu 22.04 and Python 3.10
* [Install MySQL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04)
* Clone this repository
```bash
$ git clone https://github.com/kn1-gh7/URLShortener-ITW2.git
$ cd URLShortener-ITW2
```
* Create a python virtual environment and activate it
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
* Install build dependencies
```bash
(venv)$ sudo apt update
(venv)$ sudo apt install python3.10-dev libmysqlclient-dev build-essential
(venv)$ export MYSQL_CFLAGS="$(mysql_config --cflags)"
(venv)$ export MYSQL_LDFLAGS="$(mysql_config --libs)"
```
* Install requirements
```bash
(venv)$ pip install pip setuptools -U
(venv)$ pip install -r requirements.txt
```
* Setting database config
```bash
# After installing mysql and setting root password
(venv)$ mysql -u root -p
# Choose a database name
mysql> CREATE DATABASE urlshortener_db;
mysql> exit
# Open src/urlshortener/urlshortener/settings.py and go to the following section
..
DATABASES  = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'urlshortener_db', #Set the name of database here
		'USER': 'root',
		'PASSWORD': 'password', #Set the password for mysql root user here
		'HOST': 'localhost',
		'PORT': '3306',
	}
}
..
```
* Make migrations and run server
```bash
# In the src/urlshortener directory
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```
Done! You have the app running!
