# Voice-Activated-Desktop-Assistant-JARVIS

## Jarvis - Voice-Activated Desktop Assistant (single-file)


## Features implemented:
- speak(text): uses pyttsx3 to speak text aloud
- take_command(): uses SpeechRecognition to listen via microphone and return text
- greet_user(): greets based on current local time
- tell_time(): replies with the current time
- wikipedia_search(topic): reads first two sentences from Wikipedia
- open_website(key): opens YouTube, Google, or a LinkedIn profile (set LINKEDIN_URL)
- query_llm(prompt): integration example for OpenAI (uses OPENAI_API_KEY env var)
- note_taking: "note [text]" saves a note to notes.txt
- system_status: custom feature — shows CPU and memory usage (requires psutil)


Usage:
1) Install dependencies: pip install -r requirements.txt
requirements.txt (example):
pyttsx3
SpeechRecognition
wikipedia
PyAudio # or pipwin install pyaudio on Windows
openai
psutil

pip install pyttsx3 SpeechRecognition wikipedia webbrowser google-genai

2) Set environment variable OPENAI_API_KEY if you want LLM integration.
Example (Linux/macOS): export OPENAI_API_KEY="sk-xxx"
Windows (PowerShell): $env:OPENAI_API_KEY="sk-xxx"


3) Update LINKEDIN_URL below with your LinkedIn profile URL.



## Notes:

- Microphone and internet access required for speech recognition and Wikipedia/LLM queries.
- If pyaudio install is problematic on Windows, 
- use pipwin: 

            ```bash
            pip install pipwin; 
            pipwin install pyaudio
            ```


## 💻 Requirements 

- Python 3.11 or higher 


## How to run? 

### To select interpreter:

    - ctrl + shift + p
    - base interpreter

1. Create a virtual environment:

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