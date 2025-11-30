import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from google import genai
from google.genai.errors import APIError
import time

# --- Configuration and Initialization ---

# Initialize Text-to-Speech Engine (Level 1: The Mouth)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize Gemini Client (Level 3: The "Generative AI" Brain)
genai_client = None
model_name = 'gemini-2.5-flash'
try:
    # Client automatically picks up the GEMINI_API_KEY from environment variables.
    # *** GEMINI_API_KEY is set as an environment variable! ***
    genai_client = genai.Client()
except Exception as e:
    # This block handles the case where the API key is not found in the environment
    print(f"Error initializing Gemini client. Make sure GEMINI_API_KEY is set: {e}")


# --- Level 1: The Mouth & Ears (Basic Input/Output) ---


def speak(text):
    """Function to read the given text out loud."""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Uses microphone to listen and convert audio to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"

    return query.lower()


def wish_me():
    """Greets the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning, Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Sir!")
    else:
        speak("Good Evening, Sir!")

    speak("I am Jarvis, your personal desktop assistant. How may I help you?")

# --- Core Feature Helper Function (FIXED) ---


def generative_ai_think(prompt):
    """Sends the prompt to the Gemini LLM and speaks the answer."""
    global genai_client

    if not genai_client:
        speak("My AI thinking module is currently offline. Please check the API key setup in the environment variables.")
        return

    # Add system instruction for JARVIS persona
    system_prompt = "Your name is JARVIS, You act like JARVIS, the AI assistant from Iron Man. Answer the provided user input concisely and professionally, keeping the JARVIS persona."

    speak(f"Thinking about: {prompt}")

    try:
        response = genai_client.models.generate_content(
            model=model_name,
            contents=prompt,
            config={"system_instruction": system_prompt}
        )

        speak(response.text)

    except APIError as e:
        speak(f"I encountered an API error while trying to think. Status: {e.status_code}")
    except Exception as e:
        speak(f"An unexpected error occurred during the AI process. Error: {e}")


# --- Main Program Logic (FIXED) ---

def main_jarvis_loop():
    wish_me()

    while True:
        query = take_command()

        # Guard clause for empty or failed command recognition
        if query == "none":
            continue

        # --- Level 2: The Worker (Automation Tasks) ---

        # 1. Tell Time
        if 'what time is it' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the current time is {current_time}")

        # 2. Wikipedia Search
        elif 'wikipedia' in query:
            try:
                topic = query.replace("wikipedia", "").strip()
                if not topic:
                    speak("Please tell me what you want to search on Wikipedia.")
                    continue

                speak(f"Searching Wikipedia for {topic}...")
                results = wikipedia.summary(topic, sentences=2, auto_suggest=False)
                speak("According to Wikipedia:")
                speak(results)

            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I could not find any page for {topic} on Wikipedia.")
            except Exception as e:
                speak(f"An error occurred during the Wikipedia search: {e}")

        # 3. Web Browser Automation
        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif 'open linkedin' in query:
            # TODO: Replace with your actual LinkedIn profile URL!
            linkedin_url = "https://www.linkedin.com/in/mdasadulislam/"
            speak("Opening your LinkedIn profile.")
            webbrowser.open(linkedin_url)

        # --- Bonus Challenge: Custom Feature (Wait/Sleep Command) ---
        elif 'wait for' in query or 'sleep for' in query:
            try:
                parts = query.split()
                seconds = next((int(p) for p in parts if p.isdigit()), None)

                if seconds and seconds > 0:
                    speak(f"Going to sleep for {seconds} seconds. Wake me up later.")
                    time.sleep(seconds)
                    speak("I am back. Did you need anything while I was sleeping?")
                else:
                    speak("Sorry, I didn't understand how long you want me to wait.")
            except Exception:
                speak("I had trouble with the wait command.")

        # 4. Exit Command
        elif 'quit' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye, Sir. Have a great day!")
            break

        else:
            generative_ai_think(query)


if __name__ == "__main__":
    main_jarvis_loop()
