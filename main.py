#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################################################
## Contact point define where and how alert notifications are sent
## Contact points integrate with external services like email, SMS, or webhooks.
#################################################################################

import uuid
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

app = FastAPI()

# security scheme
security = HTTPBearer()
API_KEY =  "".join(str(uuid.uuid4()).split('-'))

@app.on_event("startup")
async def startup_event():
    print(f"🔑 API Key: {API_KEY}")
    print(f"🚀 Application started! Use this API key for authentication.")
print(f"Usage: curl -X POST http://localhost:8000/receive "
      f"-H \"Authorization: Bearer {API_KEY}\" "
      f"-H \"Content-Type: application/json\" "
      f"-d '{{\"message\": \"Hello FastAPI\" }}'")


@app.get("/")
async def root():
    return {"message": "Send POST to receive endpoint..."}

def create_twilio_client():
    import os
    from twilio.rest import Client

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    client = Client(account_sid, auth_token)


    message = client.messages.create(
        body="test alert",
        from_="+16075364794", # virtual number provided by Twilio
        to="+407287856559", # destination number
    )

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify the provided API key"""
    if credentials.scheme.lower() != "bearer" or credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key",
        )
    return credentials.credentials

@app.post("/receive")
async def receive_data(request: Request, token: str = Depends(verify_token)):
    """ Parse Grafana webhook data """
    body = await request.json()
    print("Raw incoming webhook:", body)
    # if body.get("status") == "firing":
    #     create_twilio_client()
    print ("Status:", body.get("status", "No status provided"))
    print("No of alerts:", len(body.get("alerts", [])))
    for alert in body.get("alerts", []):
        print(f"Alert: {alert.get('labels', {}).get('alertname', 'No alert name')}, "
              f"Status: {alert.get('status', 'No status')}, "
              f"Starts at: {alert.get('startsAt', 'No start time')}")   
    return {"status": "received"}


## k8s deployment
## kubectl run grafanacontactpoint --image=dejanualex/grafana_contactpoint:1.0 
## kubectl expose pod grafanacontactpoint --name=grafanacontact --type="ClusterIP" --port=8000 --target-port=8000