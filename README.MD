### Introduction  
Twittomtere is a simple web application that searches Twitter for Tweets with a given keyword, 
analysis sentiments (positive or negative) and summarize results in a histogram. Twittometer created for 
educational purposes to demonstrate how to:  
  * use APIs to get the data
  * use Natural Language Processing (NLP) to analyze text of the Tweets
  * do data visualization and develop interactive dashboard  
  * deploy the app on a cloud service to make it available for others  
  * do all of it with less than 100 lines of code  
  
### Requirements
1. Computer with installed Python 3x  
2. Email account  
3. Twitter account  
4. For cloud deployment - [PythonAnywhere](www.pythonanywhere.com) account 
(free account is good enough for the app to work as of July 2019)       
5. Optional:   
  * Git, GtiHub Desktop or any other GitHub client  
  * IDE, text/code editor  

### Getting Twitter API Access
1. Create a Twitter account if you do not have one  
2. Apply for developer account, fill the form, 
3. Wait for approval and get API access credentials  (*can take several days*)  
4. More details can be found here: https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html  
5. This API credentials will be used later

### Running Code Locally:
1. Get this repository (repo) to local machine using one of the options:
  * download repo as a zip file:  
[Click on 'Clone or download' and select zip](https://github.com/takmakov/twittometer/archive/master.zip)   
  * use command line [git](https://git-scm.com/) client:  
```
git clone https://github.com/takmakov/twittometer.git
```
  * use git client with visual interface, such as [GitHub Desktop](https://desktop.github.com/)

2. Use text/code editor, modify *twkeys.py* file to input your API credentials:  
```
C_KEY = "type yours here"  
C_SECRET = "type yours here"  
A_TOKEN = "type yours here"  
A_SECRET = "type yours here"  
```
3. Create virtual environment for this 'twenv' to avoid conflicts with other Python projects.
This is not required, but highly recommended.
Assuming Anaconda is used as a package manager   
```
conda create -n twenv --python=python3.6
```
4. Activate this environment  
  * MacOS/Linux
```
source activate twenv
```
  * Windows  
```
activate twenv
```
5. Install packages listed in requirements.txt  
```
pip install -r requirements.txt
```

6. Check that the packages are installed (the exact output may vary)  
```
(twenv)$ pip freeze
...
dash==0.43.0
dash-core-components==0.48.0
dash-html-components==0.16.0
dash-renderer==0.24.0
dash-table==3.7.0
...
plotly==2.5.1
...
textblob==0.15.3
...
tweepy==3.6.0
...
```
7. Run the app
```
python app.py
```
8. In web browser, go to [http://127.0.0.1:8050](http://127.0.0.1:8050) to access the app

9. Complimentary Jupyter Notebook [twittometer.ipynb](twittometer.ipynb) demonstrates use of *twminer* function 
including output for each Tweet


### Deployment to PythonAnywhere:

1. Create free/beginner account on PythonAnywhere
It is necessary to do everything fast, because there is only 100 sec per 24 hours of CPU time for free account  
Also, avoid installing additional packages or adding other files, because free account has only 512 Mb  

2. Open new Bash console and clone the repo  
```
git clone https://github.com/takmakov/twittometer.git
```
3. Create virtual environment using *virtualenv* tool
``` 
mkvirtualenv twenv --python=python3.6
```
4. Activate virtual environment:
```
source virtualenvwrapper.sh
workon twenv
```  
5. Install packages listed in requirements.txt
```
(twenv)~/twittometer $ pip install -r requirements.txt
```
6. Check that the packages are installed (the exact output may vary)  
```
(twenv)~ $ pip freeze
-f /usr/share/pip-wheels
attrs==19.1.0
certifi==2019.6.16
chardet==3.0.4
Click==7.0
dash==0.43.0
dash-core-components==0.48.0
dash-html-components==0.16.0
dash-renderer==0.24.0
dash-table==3.7.0
decorator==4.4.0
Flask==1.1.1
Flask-Compress==1.4.0
idna==2.8
ipython-genutils==0.2.0
itsdangerous==1.1.0
Jinja2==2.10.1
jsonschema==3.0.1
jupyter-core==4.5.0
MarkupSafe==1.1.1
nbformat==4.4.0
nltk==3.4.4
oauthlib==3.0.2
plotly==2.5.1
pyrsistent==0.15.3
PySocks==1.7.0
pytz==2019.1
requests==2.22.0
requests-oauthlib==1.2.0
six==1.12.0
textblob==0.15.3
traitlets==4.3.2
tweepy==3.6.0
urllib3==1.25.3
Werkzeug==0.15.4
(twenv) 03:32 ~ $ 
```  
### Configuring Web App  

1. Assumption: *yourusername* is your PythonAnywhere username 
2. On PythonAnywhere Dashboard, go to 'Web' tab  
3. On 'Web' tab, modify Code section
>Source code: /home/yourusername/twittometer/app.py  
>Working directory: /home/yourusername/twittometer/  
4. For WSGI file, list the following path
>WSGI configuration file:/var/www/yourusername_pythonanywhere_com_wsgi.py
5. Click on WSGI file and edit it and save it per instructions below. 
This file has a lot of information, but the only lines that we care about are shown below.
These are the lines that are uncommented (not starting with '#')  

```

HELLO_WORLD = """<html>
<head>
    <title>PythonAnywhere hosted web application</title>
</head>
<body>
<h1>Hello, World!</h1>
<p>
    This is the default welcome page for a
    <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>
    hosted web application.
</p>
<p>
    Find out more about how to configure your own web application
    by visiting the <a href="https://www.pythonanywhere.com/web_app_setup/">web app setup</a> page
</p>
</body>
</html>"""


def application(environ, start_response):
    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
        content = HELLO_WORLD
    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')

import sys

path = '/home/yourusername/twittometer'
if path not in sys.path:
    sys.path.append(path)

from app import app
application = app.server
```
6. Go back to 'Web' tab and edit virtual environments section    
>Virtualenv:  
>/home/yourusername/.virtualenvs/twenv/  
7. Proceed edit the following items adding username (SET_USERNAME) and password (SET_PASSWORD).
This is needed to minimize unathorized use of your personal API access keys  
>Force HTTPS: Enabled  
>Password protection: Enabled    
>Username: SET_USERNAME  
>Password: SET_PASSWORD    
8. Reload the app by going to the top of the 'Web' tab and clicking on a button in 'Reload' section
9. Go to yourusername.pythonanywhere.com, type the web app access credentials ('SET_USERNAME' and 'SET_PASSWORD') and enjoy the app
![Twittometer Screenshot](Twittometer.png?raw=true "Screenshot")


### Disclaimer  
This repository, code and instructions are created in my personal time for educational purposes only.   
This repository and code is not part of any of my official position(s), official duties or affiliations.
