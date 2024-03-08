from speech_recognition_handler import recognize_speech_from_mic, advanced_language_exercise
from hue_light_controller import control_light
from environmental_manager import get_current_weather  

def main():
    print("VoiceHome+ System is now active. Speak a command in Vietnamese.")
    while True:
        command = recognize_speech_from_mic()
        if command:
            if 'bật đèn' in command:
                control_light(light_id=1, state=True)  #Used to turn on light
            elif 'tắt đèn' in command:
                control_light(light_id=1, state=False)  # Used to turn off light
            elif 'thời tiết' in command:
                weather = get_current_weather("Ho Chi Minh")
                print(f"Current weather in Ho Chi Minh City is: {weather}.")
            elif 'bài tập ngôn ngữ' in command:
                advanced_language_exercise()
            else:
                print("Sorry, I didn't catch that. Can you please repeat?")
                
if __name__ == "__main__":
    main()
