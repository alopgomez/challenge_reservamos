# Challenge Reservamos
This repository contains the Weather API requested by the Reservamos coding challenge. By entering a partial or complete name of a city you may obtain the weather forecast (max and min temperature in Kelvin and Celsius) for the next 7 days of any city that matches the input query.

## Prerequisites

This project needs the following basic requirements:
  - Python 3 (code tested with version 3.12.0)
  - Libraries set forth in requirements.txt
    - asgiref (3.7.2)
    - certifi (2023.11.17)
    - charset-normalizer (3.3.2)
    - Django (5.0.1)
    - idna (3.6)
    - requests (2.31.0)
    - sqlparse (0.4.4)
    - urllib3 (2.1.0)

It is recommended to install these libraries through a python virtual environment. To create it, one could use the built-in `venv` package, e.g.
```shell
$ python -m venv env
```
where `env` is the name of the environment. This environment can be activated executing the `activate` program located in the `env` folder:
``` shell
$ cd /path/to/env
$ cd bin/
$ source activate
```

Once activated, it is straigthforward to install the libraries mentioned above,
``` shell
$ pip install -r requirements.txt
```

## Configuration

To execute the Weather API, it is necessary to explicitly specify a usable OpenWeather API key. For this, you need to create a file with the name `config.py` within the weather_app folder inside the repository's main directory
```shell
$ cd /path/to/challenge/repository
$ cd weather_app/
$ touch config.py # must be created with this name
```

Inside the `config.py`, one must enter the following,
```python
API_OPENW = 'insert_here_your_api_key'
```

The constant name `API_OPENW` must be preserved for the code to work. **Do not include the `config.py` file in your repository if you decide to make this code publicly available**.

## Running the Weather API

To run the API locally simply do the following:
```shell
$ cd /path/to/repository
$ python manage.py runserver
```

Now enter the route `127.0.0.1:8000/api/weather/` to interact with the API by entering the city or cities you wish to consult.
