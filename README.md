# Fit Fingers

## Application
![alt text](https://github.com/ayushdata/fit-fingers/blob/master/screenshots/selection.png)
-> **Homepage** <-

![alt text](https://github.com/ayushdata/fit-fingers/blob/master/screenshots/typingtest.png)
-> **Typing test** <-

![alt text](https://github.com/ayushdata/fit-fingers/blob/master/screenshots/flashgame.png)
-> **Flash typing** <-

## Requirements
- python
- pip

## Installation
First, clone this repository.
```
$ git clone https://github.com/Ayush-A/fit-fingers.git
$ cd fit-fingers
```

Create a virtual environment and activate it.
For Windows:
```
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
```

Afterwards, install all the required files:
```
$ pip install -r requirements.txt
```

Configure the application for flask.
```
$ set FLASK_APP=application.py
$ set FLASK_DEBUG=1
```

Set the API KEY for embedding Google Maps in the application
```
$ set API_KEY=YOUR_API_KEY
```

Running the web application
```
$ python -m flask run
```

To see your application running, go to:
> http://localhost:5000
