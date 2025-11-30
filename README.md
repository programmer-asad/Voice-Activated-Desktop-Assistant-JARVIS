# Voice-Activated-Desktop-Assistant-JARVIS

## Jarvis - Voice-Activated Desktop Assistant (single-file)


## Features implemented:
- speak(text): uses pyttsx3 to speak text aloud
- take_command(): uses SpeechRecognition to listen via microphone and return text
- greet_user(): greets based on current local time
- tell_time(): replies with the current time
- wikipedia_search(topic): reads first two sentences from Wikipedia
- open_website(key): opens YouTube, Google, or a LinkedIn profile (set LINKEDIN_URL)
- query_llm(prompt): integration example for Write a poem about Python, google-genai
- Bonus,Wait/Sleep,"""Jarvis, wait for 10 seconds""",time


## 💻 Requirements 

- Python 3.11 or higher 


## How to run? 

### To select interpreter:

- ctrl + shift + p
- base interpreter


1. To activate base environment:

   ```bash
   conda activate base
   ```

2. Create a virtual environment:

   ```bash
   conda create -n jarvis python=3.11 -y
   ```

3. Activate virtual environment:

   ```bash
   conda activate jarvis
   ```

4. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the JARVIS script:

   ```bash
   python jarvis.py
   ```


## For exe file conversion:

## python library

   ```bash
   pip install pyinstaller
   ```

## python command

   ```bash
   pyinstaller --onefile jarvis.py
   ```


## 👨‍💻 Author

**Md. Asadul Islam**

Inspired by Tony Stark's JARVIS


## 📜 License

This project is open-source and free to use for learning purposes.



