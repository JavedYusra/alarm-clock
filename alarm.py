from datetime import datetime
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Ask user for alarm time
alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM):\n")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

print("Setting up alarm...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")   # 12-hour format
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p") # AM or PM

    if (alarm_period == current_period and
        alarm_hour == current_hour and
        alarm_minute == current_minute and
        alarm_seconds == current_seconds):

        print("Wake Up!")
        pygame.mixer.music.load("audio.mp3")  # put your mp3/wav file here
        pygame.mixer.music.play()
        
        # Keep playing until stopped manually
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        break
