from gtts import gTTS
import os
from datetime import datetime

# Function to set the styling of the interface
def style_text(text, style):
    styles = {
        'bold': '\033[1m',
        'underline': '\033[4m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'magenta': '\033[95m',
        'white': '\033[97m',
        'black': '\033[30m',
    }
    return styles[style] + text + '\033[0m'


def generate_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    style_text('The moment\'s timestamp: {}'.format(timestamp), 'underline')
    return timestamp

# Function to get user input for text and voice features
def get_user_input(text):
    print(style_text("Text-to-Speech Generator", "bold"))
    print(style_text("Enter the following details:", "blue"))
    if not text: 
        text = input("Text to convert: ")
    language = input("Language (e.g., 'tr' for Turkish): ")
    speed = input("Speed (default is 1.0): ")
    save_as = input("Save file as (e.g., 'output'): ")

    timestamp = generate_timestamp()
    save_as = f"{save_as}---{timestamp}" if save_as else timestamp
    save_as = f"{save_as}.mp3"

    return text, language, speed, save_as

def get_input_text_from_file():
    with open('../files/input/input.txt') as f:
        input_text = f.read()
    return input_text

def confirm_loading_text_from_file():
    inp = input("Using the text in input folder. Proceed ? (y/n) =>").lower()
    if inp == 'y':
        return True
    elif inp == 'n':
        pass
        style_text('This feature is still under development. New line characters\' presence causes the program to proceed early!  ', 'cyan')
        raise Exception
    else:
        print(style_text('Loading from file.', 'red'))
        return True
# Function to generate the audio file
def generate_audio(text, language, speed, save_as):
    text = text.strip()
    tts = gTTS(text, lang=language, slow=False)
    if speed:
        tts.speed = float(speed)
    try:
        tts.save(save_as)
        print(style_text("Audio file generated successfully!", "green"))
    except Exception as e:
        print(style_text("Error occurred while saving the audio file:", "red"), str(e))


# Main function for user interaction
def main():
    if confirm_loading_text_from_file():
        text = get_input_text_from_file()
    text, language, speed, save_as = get_user_input(text)
    generate_audio(text, language, speed, save_as)


# Run the main function
if __name__ == "__main__":
    main()

