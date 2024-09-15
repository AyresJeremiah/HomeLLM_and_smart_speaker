from flask import Flask, request, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/audio', methods=['POST'])
def handle_audio():
    try:
        file = request.files['file']
        recognizer = sr.Recognizer()

        # Save the audio file temporarily
        file_path = '/tmp/received_audio.wav'
        file.save(file_path)

        # Check if the file was saved
        if not os.path.exists(file_path):
            return jsonify({"error": "File not saved"}), 500

        # Process the audio file
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_sphinx(audio)
            return jsonify({"text": text})
        except sr.UnknownValueError:
            return jsonify({"error": "Could not understand the audio"}), 400
        except sr.RequestError as e:
            return jsonify({"error": f"SpeechRecognition error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Internal server error: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
