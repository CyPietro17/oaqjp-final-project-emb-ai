""" Deploy web application using Flask. """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """ Function rendering at the home page. """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """ Function analyzing the input text and provide the correct output. """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response_1 = "For the given statement, the system response is "
    response_2 = f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
    response_3 = f"'joy': {joy} and 'sadness': {sadness}. "
    response_4 = f"The dominant emotion is {dominant_emotion}."

    return response_1 + response_2 + response_3 + response_4

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
