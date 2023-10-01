import pyttsx3, time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the speech rate to a slower value (e.g., 100 words per minute)
engine.setProperty("rate", 100)

# Text to be spoken
text = input("Enter text you want as a speech : ")

# Pause for a short duration (e.g., 1 second) before speaking the text
time.sleep(0.5)

# Convert and speak the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()