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

## Create a SuperUser
`python manage.py createsuperuser`  
use `admin` for username 


# Requirements and Iterations

## Requirements
https://trello.com/b/J8jBIkFV/something-snappy-db

## Iteration 1
- Cleaned up data
- In MySQL database
- No Frontend
- Queryable using SQL

Cleaning Up Data
- Examine
- Missing fields
	- 'Affected Relatives'. Y or N but sometimes blank
	- 'Proband'. Y or N but sometimes blank - unknown
	- 'Variant protein'.p.(=)
						p.?
						p.?
						p.(=)
						p.?
						p.(=)
						p.?, p.(=)
						NA
						p.?, ?
	- 'Evidence Codes' Some missing unknown
	- No lab number field, how would you like filled? For expansion
	- Sample type - what are these, would you like another? - unknown sample type table
	- No transcript for c. nomens and p. nomens - inlcude? What transcript?

## Validation check on the variant


## Iteration 2
- Basic frontend
- Display genes and variants within genes
- Viewing only

## Iteration 3/4
- Searching functionality
validating nomenclature

## Iteration 3/4
- Ability to add or change 

Nomenclature





# Development Notes
django-admin startproject somethingsnappydb

