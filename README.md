# grafana_contactpoint
Grafana contact point

## Setup

```bash
# install dependencies
python -m venv .fastapivevn
source .fastapivevn/bin/activate
pip install -r requirements.txt

# start grafana and web services
docker-compose -f docker-compose.yaml up --build -d
```

## Grafana config

* Get the web container name `docker ps --format "{{.Names}}"` and API key value `docker logs <container_name>`
* Create new contact point [here](http://127.0.0.1:3000/alerting/notifications/receivers/new) and 

## App

* At startup will generate an API key, used for auth, to be passed in the authorization header: Authorization: Bearer <your_api_key>
* Get data from Grafana and send it to an sms gateway/Routing PSTN or VoIP (e.g. [twilio](https://www.twilio.com/docs))


