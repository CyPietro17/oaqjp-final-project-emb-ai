import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = obj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = float(emotions['anger'])
        disgust_score = float(emotions['disgust'])
        fear_score = float(emotions['fear'])
        joy_score = float(emotions['joy'])
        sadness_score = float(emotions['sadness'])
    
        dominant_emotion = "dominant_emotion"
        dominant_score = 0.0

        for emotion in emotions:
            emotion_score = float(emotions[emotion])
            if dominant_score < emotion_score:
                dominant_score = emotion_score
                dominant_emotion = emotion

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
    
    return {
        'anger': anger_score,
        'disgust': disgust_score, 
        'fear': fear_score, 
        'joy': joy_score, 
        'sadness': sadness_score, 
        'dominant_emotion': dominant_emotion
        }