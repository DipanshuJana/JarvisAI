import os
import keyboard
import pyautogui
import time
from instabot import Bot
import webbrowser

def browserAutomation(query):
    if ('new tab' in query):
        keyboard.press_and_release('ctrl + t')
    
    if ('close tab' in query):
        keyboard.press_and_release('ctrl + w')

    if ('reload tab' in query):
        keyboard.press_and_release('ctrl + r')

    if ('brave search' in query) or ('chrome search' in query):
        newQuery = str(query)

        newQuery = newQuery.replace("brave search", "")
        newQuery = newQuery.replace("chrome search", "")
        Query = str(newQuery)

        keyboard.write(Query)
        keyboard.press('enter')

def youtubeAutomation(query):
    if ('pause' in query or 'resume' in query):
        keyboard.press('k')
    
    if ('full screen' in query):
        keyboard.press('f')
    
    if ('mute' in query or 'unmute' in query):
        keyboard.press('m')
    
    if ('cinema mode' in query):
        keyboard.press('t')

    if ('skip' in query):
        keyboard.press('l')
    
    if ('back' in query):
        keybaord.press('j')

    if ('increase speed' in query):
        keyboard.press_and_release('SHIFT + >')

    if ('decrease speed' in query):
        keyboard.press_and_release('SHIFT + <')

    if ('previous video' in query):
        keyboard.press_and_release('SHIFT + p')
    
    if ('next video' in query):
        keyboard.press_and_release('SHIFT + n')

    if ('search' in query):
        pyautogui.click(x=483, y=86)
        keyboard.write(query.replace("search", ""))
        time.sleep(1)
        keyboard.press('enter')

def notepadAutomation(query):
    if ('create' in query):
        return 'What will be the content of the file?'
        contents = takeCommand()
        if ('JarvisNotes' not in os.listdir()):
            os.mkdir('JarvisNotes')

        os.chdir('JarvisNotes')
        txtFiles = [files for files in os.listdir() if (os.path.splitext(files)[0] == 'JarvisNote') and (os.path.splitext(files)[1] == '.txt')]
        with open(f'JarvisNote({len(txtFiles) + 1}).txt', 'a') as txt:
            txt.write(contents)
        
        return 'Successfully created your file'
    
    if ('open' in query) and ('.txt' in query):
        return f'{query.replace("open", "")} in open now.'
        openTxt = subprocess.Popen(f'JarvisNotes\\{query.replace("open", "")}')

def instagramAutomation(query):
    username = 'your_username'
    password = 'your_password'
    bot = Bot()
    bot.login(username= username, password= password)

    if ('check my instagram messages' in query):
        webbrowser.open_new_tab('www.instagram.com')
        pyautogui.click(x=888, y=89)

    if ('follow' in query):
        user = query.replace("follow", "").strip()
        bot.follow(user)

    if ('unfollow' in query):
        user = query.replace("follow", "").strip()
        bot.unfollow(user)

    if ('send a message to' in query) or ('send a message' in query):
        try:
            newQuery = str(query)
            newQuery = newQuery.replace("send a message to", "")
            newQuery = newQuery.replace("send a message", "")
            user = str(newQuery)

            return 'What will be the message?'
            
            message = takeCommand()

            bot.send_message(message, user)
            return f'Successfully sent message to {user}'
            
        except Exception as e:
            return "Sorry, I can't send the message."

    if ('followers' in query):
        followers = bot.get_user_followers(username)
        iterate = 1
        
        for follower in followers:
            return f'{iterate}: {bot.get_user_info(follower)}'
            iterate+= 1