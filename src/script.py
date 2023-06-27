from gtts import gTTS
import os


# Function to set the styling of the interface
def style_text(text, style):
    styles = {
        'bold': '\033[1m',
        'underline': '\033[4m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
    }
    return styles[style] + text + '\033[0m'


# Function to get user input for text and voice features
def get_user_input():
    print(style_text("Text-to-Speech Generator", "bold"))
    print(style_text("Enter the following details:", "blue"))
    
    text = input("Text to convert: ")
    language = input("Language (e.g., 'tr' for Turkish): ")
    speed = input("Speed (default is 1.0): ")
    save_as = input("Save file as (e.g., 'output.mp3'): ")

    return text, language, speed, save_as


# Function to generate the audio file
def generate_audio(text, language, speed, save_as):
    tts = gTTS(text, lang=language, slow=False)
    if speed:
        tts.speed = float(speed)
    tts.save(save_as)
    print(style_text("Audio file generated successfully!", "green"))


# Main function for user interaction
def main():
    text, language, speed, save_as = get_user_input()
    generate_audio(text, language, speed, save_as)


# Run the main function
if __name__ == "__main__":
    main()

