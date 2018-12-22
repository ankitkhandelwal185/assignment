# assignment

To install packages  
pip install -r /path/to/requirement.txt 

Change the user and password of db accordingly in settings.py  


To make db migrations, run these commands  

python manage.py makemigrations college  
python manage.py migrate 

#urls  
http://localhost:8000/api/add/college  
http://localhost:8000/api/get/college/college-id  
http://localhost:8000/api/add/course  
http://localhost:8000/api/all/course  
