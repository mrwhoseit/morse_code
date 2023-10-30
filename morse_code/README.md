
Morse Code

---

# Morse Code Translator with Raspberry Pi and Buzzer

## Overview

This Python program translates text input into Morse code and outputs the Morse code pattern through a Raspberry Pi-connected buzzer. It utilizes the RPi.GPIO library to control the GPIO pins on a Raspberry Pi board.

## Components Used

- **RPi.GPIO Library:** A Python library for controlling General Purpose Input Output (GPIO) pins on Raspberry Pi.
- **Buzzer:** A simple electronic component that produces sound when an electrical current passes through it.
- **Morse Code Dictionary:** A dictionary mapping characters to their Morse code representations.

## How It Works

1. **Import Necessary Libraries:**
   - `RPi.GPIO` library is imported to handle GPIO operations.
   - `time` module is imported for time-related functions.

2. **Define Constants:**
   - `BUZZER_PIN` is set to the GPIO pin number of your choice to which the buzzer is connected.
   - `BUZZER_FREQUENCY` is set to 1000 Hz, defining the frequency of the buzzer sound.

3. **Define Morse Code Functions:**
   - `buzz_morse_code(morse_code)`: This function takes Morse code input and generates corresponding buzz patterns on the buzzer. It handles dots, dashes, and pauses between symbols and words.

   - `text_to_morse(text)`: This function converts input text to Morse code using the `morse_code_dict`. Spaces between words are represented as spaces in Morse code.

4. **User Input and Output:**
   - The program prompts the user to enter text for translation to Morse code.
   - It translates the input text to Morse code using the `text_to_morse` function.
   - The translated Morse code is printed to the console.

5. **Buzzer Output:**
   - The program then outputs the Morse code pattern to the buzzer using the `buzz_morse_code` function, generating corresponding sounds for dots, dashes, and pauses.

6. **Exception Handling:**
   - The program handles a KeyboardInterrupt exception, allowing the user to exit the program gracefully by pressing Ctrl+C.

7. **Cleanup:**
   - Finally, the program ensures cleanup by calling `GPIO.cleanup()` to reset the GPIO configuration.

## How to Use

1. **Connect Buzzer:**
   - Connect a buzzer to the Raspberry Pi GPIO pin number specified in `BUZZER_PIN`.

2. **Run the Program:**
   - Execute the Python script.
   - Enter the text you want to translate into Morse code when prompted.

3. **Listen to Morse Code:**
   - The program will output the Morse code pattern through the buzzer, allowing you to hear the translated message.

4. **Exit the Program:**
   - To exit, press Ctrl+C
