

import json
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector


app=Flask("project")

@app.route("/emotionDetector")
def emo_detector():
    """function to send text to the detector function"""
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    if response["dominant_emotion"] == 'None':
        return "Invalid text! Please try again!"
    return response


@app.route("/")
def render_index_page():
    """function to return index html file"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
