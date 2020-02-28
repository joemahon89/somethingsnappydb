# somethingsnappydb






## Installation Instructions

Clone the repository
`git clone https://github.com/joemahon89/somethingsnappydb.git`

### Installing MySQL
Create virtual environment  
Install requirements  
Install mysql packages   
`sudo apt-get install python3-dev libmysqlclient-dev`  
Install mysql server (May need to set the password)  
`sudo apt-get install mysql-server`  

### Installing Python Packages
Install mysql python packages   
`pip install mysqlclient`  
`pip install django`  

### Creating the Database
`mysql -u root -p`  
Enter password  
`CREATE DATABASE somethingsnappydb`;  
`CREATE USER somethingsnappy_user@localhost IDENTIFIED BY 'password_in_quotes';`  
`GRANT ALL PRIVILEGES ON somethingsnappydb.* TO somethingsnappy_user@localhost;`  
`FLUSH PRIVILEGES;`  
`quit`

### Create the Credentials File
This file is outside of version control but a template is provided  
Make a copy of `credentials_template.ini` called `credentials.ini`  
Fill out the correct password and save  

Check that this has all worked correctly
`python manage.py check`  
`python manage.py makemigrations`  
`python manage.py migrate`  

### Create a SuperUser
`python manage.py createsuperuser`  
use `admin` for username 


## Requirements and Iterations

### Requirements Kanban Board
https://trello.com/b/J8jBIkFV/something-snappy-db

### Iteration 1
- Cleaned up data  
- In MySQL database  
- No Frontend  
- Queryable using SQL  

### Iteration 2
- Basic frontend  
- Display:  
	- All variants  
	- All patients  
	- variants at a position  
- Viewing only  

### Iteration 3/4
- Metrics around data
- Metrics around data quality
- Searching functionality  

### Future Iterations
- Ability to add or change variants within the web interface  
- Validating nomenclature  
- Creation of new HGVS c. and p. nomenclature  
- Logins and access control




## User Guide
This database contains information about variants that have been detected.  


