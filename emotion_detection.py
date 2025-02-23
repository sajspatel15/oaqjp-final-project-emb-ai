"""Module to run the emotion detection software from"""
import requests
import json

def emotion_detector(text_to_analyze: str):
    """
    Emotion detector that will run analysis on the text passed in.
    :param text_to_analyze: the input string to run emotion detection on.
    :return the emotion of the text.
    """
    # url to send 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # headers to include in the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # json object to pass into the request
    req_obj = {"raw_document": {"text": text_to_analyze} }

    # make the post request to with the given text
    response = requests.post(url, json=req_obj, headers=headers)
    # create a formatted response stored in a dict
    formatted_response = json.loads(response.text)

    # check for valid response and format output appropriately
    if response.status_code == 200:
        formatted_response = formatted_response['emotionPredictions'][0]['emotion']
    # check if a 500 error was recieved
    elif response.status_code == 500:
        formatted_response = None

    # returning the formatted response
    return formatted_response