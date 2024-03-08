
import speech_recognition as sr

def recognize_speech_from_mic(language='en-US'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust depending on ambient noise levels
        print(f"Listening for commands in {language}...")
        audio = recognizer.listen(source)

        try:
            # Language parameter allows switching between Vietnamese and English
            speech_text = recognizer.recognize_google(audio, language=language)
            print(f"Interpreted Command: {speech_text}")
            return {'success': True, 'error': None, 'transcription': speech_text.lower()}
        except sr.UnknownValueError:
            return {'success': False, 'error': "Unable to understand the command", 'transcription': None}
        except sr.RequestError as e:
            return {'success': False, 'error': f"API request failed: {e}", 'transcription': None}
