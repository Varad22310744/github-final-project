import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {'error': 'Input text cannot be empty'}

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        emotions = data['emotionPredictions'][0]['emotion']
        return emotions
    else:
        return {'error': 'Request failed with status code {}'.format(response.status_code)}
