from speech_recognition_handler import recognize_speech_from_mic
from hue_light_controller import control_light, set_brightness, set_color_temp, get_light_status

def process_command(command_info):
    if command_info['success']:
        command = command_info['transcription']
        if 'turn on' in command:
            control_light(1, True)
        elif 'turn off' in command:
            control_light(1, False)
        elif 'brightness' in command:
            # Extracting brightness level from command could involve additional NLP
            set_brightness(1, 200)  # Example: Set to 200, adjust as needed
        elif 'temperature' in command:
            set_color_temp(1, 400)  # Example: Set to 400, adjust as needed
        elif 'status' in command:
            get_light_status(1)
        # Add more conditional branches for different commands
        else:
            print(f"Sorry, I didn't understand the command: {command}")
    else:
        print(f"Error: {command_info['error']}")

def main():
    language_mode = 'en-US'  # Default to English; switch to 'vi-VN' for Vietnamese
    print("VoiceHome+ started. Say 'switch language' to change modes.")
    
    while True:
        command_info = recognize_speech_from_mic(language=language_mode)
        if command_info['transcription'] == 'switch language':
            language_mode = 'vi-VN' if language_mode == 'en-US' else 'en-US'
            print(f"Switched language mode to {language_mode}.")
            continue  # Skip further processing and listen for the next command
        process_command(command_info)

if __name__ == "__main__":
    main()
