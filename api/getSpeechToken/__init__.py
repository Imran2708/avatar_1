import logging
import requests
import os

import azure.functions as func

# Define subscription key and region
subscription_key = os.getenv("AZURE_SPEECH_API_KEY")
region = os.getenv("AZURE_SPEECH_REGION")
azure_speech_endpoint = os.getenv("AZURE_SPEECH_ENDPOINT")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == 'POST':
        # Define token endpoint
        token_endpoint = f"https://{region}.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        response = requests.post(token_endpoint, headers={"Ocp-Apim-Subscription-Key": subscription_key})
        if response.status_code == 200:
            access_token = response.text
            return func.HttpResponse(
                access_token,
                status_code=200
            )
        else:
            return func.HttpResponse(response.status_code)
    else:
        return func.HttpResponse("Method Not Allowed", status_code=405)
