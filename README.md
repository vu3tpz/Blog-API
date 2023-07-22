# Blog-API

Simple Blog API that have similar functionality like Instagram

# Build with ⚒️

-> [**Django FrameWork**](https://www.djangoproject.com/) | [**Django Rest FrameWork**](https://www.django-rest-framework.org/)

-> [**SQLite**](https://www.sqlite.org/) 

-> [**Pre-Commit**](https://pre-commit.com/)

# How to run Locally 🖥️

1. Before the following steps make sure you have [git](https://git-scm.com/downloads) installed on your system.


2. Download and Install [Python](https://www.python.org/) required version.


3. Read about [virtualenv](https://docs.python.org/3/tutorial/venv.html) in Python. Create a virtual environment for your project.


```
pip install virtualenv
```
```
virtualenv virtualenv_name
```


4. Activate the environment in cmd.

**For Windows**
```
virtualenv_name\scripts\activate
```


**For Ubuntu**
```
source virtualenv_name/bin/activate
```


Clone the GitHub project in your local directory with command `git clone https://github.com/vu3tpz/Blog-API` or you can just download the code and unzip it. 


```
git clone https://github.com/vu3tpz/Blog-API
```


5. Run the command in console `pip install -r requirements.txt`  go to that directory and run the above command. This command will install the necessary packages required to run the project.


```
pip install -r requirements.txt
```


6. Go the the directory where `manage.py` file is present. Run following commands in the cmd


```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```


7. You can Run Your API in [**Postman**](https://www.postman.com/)



## The End..⚔️
