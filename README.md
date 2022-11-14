# weather-app

An API for fetching the weather forecast for a given city over a period of days.

## Requirements

- Ideally a Linux/Unix environment 
- Python 3.10 +

## Setup (Unix/Linux)

1. Clone the project.

2. Setup and activate a virtual environment.
    ```bash 
    python -m virtualenv venv
    
    source venv/bin/activate   
    ```
3. Install dependencies.
    ```bash 
    pip install -r requirements.txt 
    ```
4. (Optional) Add your own API key for [weatherapi.com](https://www.weatherapi.com/) to environment using the name `WEATHER_APP_API_KEY`. You'll only need to do this if the included key has expired.

## Usage

1. Run the server
    ```bash 
    python manage.py runserver 
    ```
2. Call forecast API using your favourite client e.g
    ```bash 
    GET http://127.0.0.1:8000/api/locations/<city>

    GET http://127.0.0.1:8000/api/locations/london
    ```

    or

    ```bash 
    GET http://127.0.0.1:8000/api/locations/<city>/?days={number_of_days} 

    GET http://127.0.0.1:8000/api/locations/london/?days=10
    ```

## Tests

```bash 
 python manage.py test   
```


## Coverage

```bash 
coverage run --source='.' manage.py test              

coverage report   
```

## API Docs

Browse to:
```
GET http://127.0.0.1:8000/api/locations/<city>

GET http://127.0.0.1:8000/api/locations/london
```
