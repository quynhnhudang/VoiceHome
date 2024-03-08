import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your command...")
        audio = recognizer.listen(source)

        try:
            speech_text = recognizer.recognize_google(audio)
            print(f"Command received: {speech_text}")
            return speech_text.lower()
        except sr.UnknownValueError:
            return "I couldn't understand that."
        except sr.RequestError:
            return "Speech service error."

def process_command(raw_text):
    return raw_text.lower()
