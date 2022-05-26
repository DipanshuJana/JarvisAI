from webData import *
from appData import *
from Automations import *
from Calculator import *
from datetime import datetime
from playsound import playsound
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import smtplib
import geocoder
import speech_recognition as sr
import time
import pywhatkit
import webbrowser
import os
import pyautogui
import pyttsx3
import speake3
import platform
import subprocess
import re
import pyjokes
import requests
import json
import speedtest
import wolframalpha

# initialize pyttsx3 engine
engine = speake3.Speake()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# main speak function
def speak(text):
    engine.say(text)
    engine.talkback()

# takes the command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language= 'en-in')
            print (f'User said: {query}\n')
        except Exception as e:
            print (e)
            return 'None'
        return query

# wishes the user according to the time
def wishUser():
    if (datetime.now().hour > 6) and (datetime.now().hour < 12):
        print ('Good Morning Sir, How can I help you?')
        speak ('Good morning sir, how can I help you?')

    if (datetime.now().hour > 12) and (datetime.now().hour < 17):
        print ('Good Afternoon Sir, How can I help you?')
        speak ('Good afternoon sir, how can I help you?')

    if (datetime.now().hour > 17) and (datetime.now().hour < 21):
        print ('Good Evening Sir, How can I help you?')
        speak ('Good evening sir, how can I help you?')

# sets the alarm
def alarmClock(time):
    Hour = int(time[0])
    Minute = int(time[1])
    Period = time[2]

    if (Period == 'PM'):
        Hour += 12
    
    while (True):
        if (datetime.now().hour == Hour) and (datetime.now().minute == Minute):
            print (f'you had set your alarm at {Hour}:{Minute}...')
            playsound('Alarm.mp3')
            reply = takeCommand()
            if ('stop' in reply):
                quit()
# speaks news using api
def speakNews():
    try:
        apiKey = 'your_api_key'

        print ("News for today...")
        speak ("News for today.")
        url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}'

        news = requests.get(url).text
        news_json = json.loads(news)

        articles = news_json['articles']

        index = 1

        for i in articles:
            print (f"{index} : {i['title']}")
            speak (i['title'])
            time.sleep(1)
            index += 1
        print ('The news has ended.Thanks for listening.')
        speak ('The news has ended. Thanks for listening.')
    except Exception as e:
        print ("I Can't fetch data from the server.")
        speak ("I Can't fetch data from the server.")

# shows a specific place on google map and says the distance from the the current place to the specific place
def googleMaps(place):
    url = f'https://www.google.com/maps/place/{place}'
    webbrowser.open_new_tab(url)
    
    try:
        geolocator = Nominatim(user_agent='myGeocoder')
        targetLocation = geolocator.geocode(place, addressdetails= True)
        target_lat_long = targetLocation.latitude, targetLocation.longitude
        targetLocation = targetLocation.raw['address']
        target = {
            'City': targetLocation.get('city', ''),
            'State': targetLocation.get('state', ''),
            'Country': targetLocation.get('country', ''),
        }

        myLocation = geocoder.ip('me')
        current_lat_long = myLocation.latlng

        distance = str(great_circle(current_lat_long, target_lat_long))
        distance = str(distance.split(' ', 1)[0])
        distance = round(float(distance), 2)

        for data in target:
            print (f'{data}: {target[data]}')
        speak(target)

        print (f'{place} is {distance} Kilometres away from you.')
        speak (f'{place} is {distance} Kilometres away from you.')
    except Exception as e:
        print ("Can't calculate the distance.")
        speak ("Can't calculate the distance.")

# says the current location
def currentLocation():
    try:
        ip = requests.get('https://api.ipify.org').text

        url = f'https://get.geojs.io/v1/ip/geo/{ip}.json'

        data = requests.get(url)
        location = data.json()

        city = location['city']
        country = location['country']

        print (f'Your current location is {city}, {country}.')
        speak (f'Your current location is {city}, {country}.')

        webbrowser.open_new_tab('your location')
        time.sleep(5)
    except Exception as e:
        print ("Can't find your current location.")
        speak ("Can't find your current location.")     

# says current temperature
def currentTemperature(data):
    apiKey = 'your_api_key'
    data = wolframalpha.Client(apiKey)
    parsedData = data.query(query)

    try:
        temp = next(parsedData.results).text

        print (f'{data} is {temp}.')
        speak (f'{data} is {temp}.')

    except:
        print ("I couldn't get any information of your specified place.")

# sends email
def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    serve.login('senderemail@gmail.com', 'email_password')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishUser()
    System = platform.uname()

    while (True):
        query = takeCommand().lower()

        print (instagramAutomation(query))
        speak (instagramAutomation(query))
        print (notepadAutomation(query))
        speak (notepadAutomation(query))
        print (calculate(query))
        speak (calculate(query))
        browserAutomation(query)
        youtubeAutomation(query)

        if ('news' in query):
            speakNews()

        if ('introduce yourself' in query) or ('what can you do for me' in query):
            print ('Hello Sir, I am Jarivs, your personal assistant. I can help you do some boring daily tasks if you are feeling lazy.')
            speak ('Hello sir, I am Jarivs, your personal assistant. I can help you do some boring daily tasks if you are feeling lazy.')
        
        if ('who made you' in query) or ('who created you' in query):
            print ('Dipanshu Jana has made me.')
            speak ('Dipanshu Jana has made me.')

        if ('info' in query) or ('system information' in query):
            print (f"System: {System.system}")
            speak (f"System: {System.system}")
            print (f"Node Name: {System.node}")
            speak (f"Node Name: {System.node}")
            print (f"Release: {System.release}")
            speak (f"Release: {System.release}")
            print (f"Version: {System.version}")
            speak (f"Version: {System.version}")
            print (f"Machine: {System.machine}")
            speak (f"Processor: {System.processor}")

        if ('joke' in query) or ('make me laugh') in query:
            try:
                joke = pyjokes.get_joke(language='en', category='all')
                print (joke)
                speak (joke)
            except Exception as e:
                print ("Can't find a joke.")
                speak ("Can't find a joke.")

        if ('youtube search' in query):
            try:
                print ('Searching Youtube...')
                speak ('Searching Youtube...')
                webbrowser.open_new_tab(f'https://www.youtube.com/results?search_query={query.replace("youtube search", "")}')
                time.sleep(2)
                speak('This might also help you.')
                pywhatkit.playonyt(query.replace("youtube search", ""))
            except Exception as e:
                print (f'Unable to search {query.replace("youtube search", "")} on Youtube.')
                speak (f'Unable to search {query.replace("youtube search", "")} on Youtube.')

        if ('google search' in query):
            try:
                print ('Searching Google...')
                speak ('Searching Google...')
                time.sleep(2)
                webbrowser.open_new_tab(f'https://www.google.com/results?search_query={query.replace("google search", "")}')
            except Exception as e:
                print (f'Unable to search {query.replace("google search", "")} on Google.')
                speak (f'Unable to search {query.replace("google search", "")} on Google.')

        if ('meaning of' in query):
            try:
                print ('Here is what I found...')
                speak ('Here is what I found...')
                webbrowser.open_new_tab(f'https://www.google.com/results?search_query={query.replace("meaning of", "")}')
            except Exception as e:
                print (f"Can't find the meaning of {query.replace('meaning of', '')} from the internet.")
                speak (f"Can't find the meaning of {query.replace('meaning of', '')} from the internet.")

        if ('set alarm at' in query) or ('set alarm for' in query) or ('set alarm' in query):
            time = re.findall('[0-9]+', query)
            if 'p.m.' in query:
                time.append('PM')
            elif 'a.m.' in query:
                time.append('AM')
            alarmClock(time)

        if ('screenshot' in query) or ('capture' in query):
            try:
                time.sleep(1)
                myScreenshot = pyautogui.screenshot()
                if 'Screenshots' not in os.listdir():
                    os.mkdir('Screenshots')
                    
                os.chdir('Screenshots')
                captures = [images for images in os.listdir() if ('JarvisCapture' in os.path.splitext(images)[0]) and (os.path.splitext(images)[1] == '.png')]
                myScreenshot.save(f'D:\\JarvisAI\\Screenshots\\JarvisCapture({len(captures)+1}).png')
                print ('Successfully captured screenshot.')
                speak ('Successfully captured screenshot.')
            except Exception as e:
                print ("Oops, I can't capture the screenshot.")
                speak ("Oops, I can't capture the screenshot.")

        if ('play' in query):
            print (f'Playing {query.replace("play", "")} from Youtube.')
            speak (f'Playing {query.replace("play", "")} from Youtube.')
            pywhatkit.playonyt(query.replace("play", ""))
            time.sleep(1)

        if ('open' in query):
            try:
                webbrowser.open(siteList[checkWebDict(siteList, query)])
                print (f'{checkWebDict(siteList, query).capitalize()} is open now.')
                speak (f'{checkWebDict(siteList, query).capitalize()} is open now.')
                time.sleep(5)
            except Exception as e:
                if (System.system == 'Windows'):
                    print (f'{checkWinAppDict(winAppList, query).capitalize()} is open now.')
                    speak (f'{checkWinAppDict(winAppList, query).capitalize()} is open now.')
                    openApp = os.startfile(winAppList[checkWinAppDict(winAppList, query)])
                elif (System.system == 'Linux'):
                    print (f'{checkLinuxAppDict(linuxAppList, query).capitalize()} is open now.')
                    speak (f'{checkLinuxAppDict(linuxAppList, query).capitalize()} is open now.')
                    openApp = os.startfile(linuxAppList[checkLinuxAppDict(linuxAppList, query)])
                else:
                    print ('Your Operating System is not suppoted.')
                    speak ('Your operating system is not suppoted.')
            else:
                print ("Error can't open the specific query.")
                speak ("Error can't open the specific query.")

        if ('current location' in query):
            currentLocation()

        if ('show' in query):
            newQuery = str(query)

            newQuery = newQuery.replace("show", "").strip()
            newQuery = newQuery.replace("show me", "").strip()
            newQuery = newQuery.replace("in google maps", "").strip()
            newQuery = newQuery.replace("on google maps", "").strip()
            newQuery = newQuery.replace("show me where is", "").strip()

            Query = str(newQuery)
            googleMaps(Query)

        if ('internet speed' in query) or ('internet connection' in query):
            try:
                connection = speedtest.Speedtest()
                print ('Connecting to server...')

                connection.get_best_server()
                upload = connection.upload()
                download = connection.download()
                upSpeed = int(int(upload)/80000)
                downSpeed = int(int(download)/80000)

                ping = connection.results.ping
                print (f'Download Speed: {downSpeed}MB/s \nUpload speed: {upSpeed}MB/s \nPing: {ping}\n')
                speak (f'Download Speed: {downSpeed}MB/s \nUpload speed: {upSpeed}MB/s \nPing: {ping}')
            except Exception as e:
                print ("Can't connect to the server.")
                speak ("Can't connect to the server.")

        if ('temperature' in query):
            newQuery = str(query)
            newQuery = newQuery.replace("temperature", "").strip()
            newQuery = newQuery.replace("temperature in", "").strip()
            newQuery = newQuery.replace("temperature of", "").strip()

            Query = str(newQuery)

            if ('outside' in query):
                default = 'Temperature in Kolkata'
                currentTemperature(default)
            else:
                currentTemperature(f'Temperature in {Query}')

        if ('send email' in query):
            try:
                print ('What should I say?')            
                speak ('What should I say?')
                content = takeCommand()
                to = 'reciversemail@gmail.com'
                sendEmail(to, content)
                print ('Email has been sent successfully.')
                speak ('Email has been sent successfully.')
            except Exception as e:
                print ("I can't send the email.")
                speak ("I can't send the email.")