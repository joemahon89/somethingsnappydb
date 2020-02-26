# somethingsnappydb






# Installation

Clone repository
`git clone https://github.com/joemahon89/somethingsnappydb.git`


## Installing MySQL
Create virtual environment
Install requirements
Install mysql packages 
`sudo apt-get install python3-dev libmysqlclient-dev`
Install mysql server (May need to set the password)
`sudo apt-get install mysql-server`

## Installing Python Packages
Install mysql python packages 
`pip install mysqlclient`
`pip install django`


## Create the database
`mysql -u root -p`
Enter password
`CREATE DATABASE somethingsnappydb`;
`CREATE USER somethingsnappy_user@localhost IDENTIFIED BY 'password_in_quotes';`
`GRANT ALL PRIVILEGES ON somethingsnappydb.* TO somethingsnappy_user@localhost;`
`FLUSH PRIVILEGES;`
`quit`

## Create the credentials file
Make a copy of `credentials_template.ini` called `credentials.ini`
Fill out the correct password and save

Check its all worked
`python manage.py check`
`python manage.py makemigrations`
`python manage.py migrate`



# Requirements and Iterations

## Requirements


## Iteration 1


## Iteration 2


## Iteration 3


## Iteration 4








# Development Notes
django-admin startproject somethingsnappydb

