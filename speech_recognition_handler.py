import speech_recognition as sr
from random import choice

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your command (Vietnamese)...")
        audio = recognizer.listen(source)
        try:
            speech_text = recognizer.recognize_google(audio, language='vi-VN')
            return speech_text.lower()
        except sr.UnknownValueError:
            print("I couldn't understand that.")
            return None
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
            return None

def advanced_language_exercise():
    exercises = [
        {"prompt": "Increase the brightness", "keywords": ["tăng", "độ sáng"]},
        {"prompt": "Decrease the volume", "keywords": ["giảm", "âm lượng"]},
        # Add more exercises as needed
    ]
    exercise = choice(exercises)
    print(f"Please construct a sentence using the phrase (in Vietnamese): '{exercise['prompt']}'")
    response = recognize_speech_from_mic()
    if response and all(keyword in response for keyword in exercise['keywords']):
        print("Excellent! You've correctly used all the keywords.")
    else:
        print("Try again, and remember to use all the required keywords.")
