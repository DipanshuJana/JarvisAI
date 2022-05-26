This is my personal assistant which I made using Python.

Descrition:

My JarvisAI can do the following things:

Browser Automation
Youtube Automation
Notepad Automation
Instagram Automation
Sets Alarm
Speaks News
Opens Websites and Software in the system (if included inside the database - appData.py | webData.py)
Google Maps Functionality
Performs
Tells the speed of internet
Speaks about system information
Tells Random Jokes
Speaks Temperature
Send Emails

Requirements for running JarvisAI on your computer:

pip install keyboard
pip install pyautogui
pip install instabot
pip install playsound
pip install geopy
pip install geocoder
pip install wolframalpha
pip install pyjokes
pip install speechRecognition
pip install pywhatkit
pip install speedtest-cli
pip install pyttsx3 (For Windows User)
pip install speake3 (For Linux User)

Windows Users:
Install PyAudio using the following commands:

pip install pipwin
pipwin install pyaudio

Open 'App.py' and remove everything from line number 26 to 36. And paste the code written below:


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


Linux Users:
Install PyAudio using the following commands:

Ubuntu Linux: sudo apt-get portaudio19-dev python-pyaudio
        pip install pyaudio

OpenSuse Linux: sudo zypper install portaudio-devel
          pip install pyaudio

Arch Linux: pip install pyaudio
