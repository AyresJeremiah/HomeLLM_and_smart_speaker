import speech_recognition as sr
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/audio', methods=['POST'])
def handle_audio():
    file = request.files['file']
    recognizer = sr.Recognizer()
    
    # Save the audio file
    file.save('/tmp/received_audio.wav')

    # Process the audio file
    with sr.AudioFile('/tmp/received_audio.wav') as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return jsonify({"text": text})
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand the audio"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
