from flask import Flask, request, jsonify
from flask_cors import CORS   # <-- ADD THIS
from datetime import datetime
import pygame
import time
import threading

app = Flask(__name__)
CORS(app)  # <-- ENABLE CORS
pygame.mixer.init()

def alarm_checker(alarm_time, period):
    while True:
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        if current_time == f"{alarm_time} {period}":
            print("⏰ Wake up!")
            pygame.mixer.music.load("audio.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break
        time.sleep(1)

@app.route("/set_alarm", methods=["POST"])
def set_alarm():
    data = request.get_json()
    alarm_time = data.get("time")
    alarm_period = data.get("period")
    
    if not alarm_time or not alarm_period:
        return jsonify({"message": "Invalid time format"}), 400

    t = threading.Thread(target=alarm_checker, args=(alarm_time, alarm_period))
    t.start()
    
    return jsonify({"message": f"Alarm set for {alarm_time} {alarm_period}"})

if __name__ == "__main__":
    app.run(debug=True)
