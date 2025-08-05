# grafana_contactpoint
Grafana contact point

## Setup

```bash
# install dependencies
python -m venv .fastapivevn
source .fastapivevn/bin/activate
pip install -r requirements.txt

# start grafana and service
docker-compose -f docker-compose.yaml up --build -d
```

## App

* At startup will generate an API key, used for auth, to be passed in the authorization header: Authorization: Bearer <your_api_key>
* Get data from Grafana and send it to a sms gateway
