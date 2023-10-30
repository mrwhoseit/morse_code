import RPi.GPIO as GPIO
import time

# Define GPIO pin for the buzzer
BUZZER_PIN = 17

# Define buzzer frequency (in Hz)
BUZZER_FREQUENCY = 1000  # Change this value to adjust the frequency

# Morse code dictionary and other functions remain the same...

def buzz_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.1)  # Duration for dot (adjust as needed)
        elif symbol == '-':
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.3)  # Duration for dash (adjust as needed)
        else:
            time.sleep(0.1)  # Pause between words

        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.1)  # Pause between symbols

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def text_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
        else:
            morse_code += ' '
    return morse_code

def buzz_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(0.1)
        elif symbol == '-':
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            time.sleep(0.1)
        else:
            time.sleep(0.1)

try:
    # Get user input
    text_to_translate = input("Enter the text to translate to Morse code: ")
    morse_code = text_to_morse(text_to_translate)
    print("Morse Code: ", morse_code)
    
    # Output Morse code to buzzer
    buzz_morse_code(morse_code)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
