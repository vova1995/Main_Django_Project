Hello my name is Volodymyr.
There are a few steps in order to launch this project:
1) You need to have git hub installed on your computer and then you need to clone this project using command: git clone git@github.com:vova1995/Main_Django_Project.git
2) Then you have to go directly to the folder mysite and there enter command:
python manage.py runserver
3)You need to enter into searching field in google or any other searching systems defauld ip adress http://127.0.0.1:8000/


python -m smtpd -n -c DebuggingServer localht:10 this link allows u to see message for changing password


Ubuntu
use virtualenv
command: virtualenv venv
than activate virtualenv
command: source venv/bin/activate
install django 1.9.7
command: pip install Django==1.9.7
create django project
command django-admin startproject mysite
create first app
command: python ./manage.py startapp catalog
create second one
command: python ./manage.py startapp my_app

than create superuser
python3 manage.py createsuper 
login: admin
password: admin12345

we need to create templates in such way my_rep/templates/my_rep and i this case django is able to see html files and we should update setting.py

static and media files, we need to add to base.html load static in order to django will be able to see static folder and we need to add 2 variable into setting.py bse dir static and media

after you add media rout we can create in models image uploader in such way: create class and add variable for example image = models.ImageField(upload_to='name of the repository in media folder') and than we shoul do migrations

install django rest framework
commands:
pip install djangorestframework
additional packages
pip install markdown  
pip install pyyaml    
pip install django-filter  
can be download from github:
git clone git@github.com:tomchristie/django-rest-framework.git
cd django-rest-framework
pip install -r requirements.txt
pip install -r optionals.txt



used importin to db from csv files
file import.python3

if u forget admin password i recommend u a great topic : https://www.laurivan.com/change-a-django-password-manually/