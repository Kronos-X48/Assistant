import pyttsx3
import os
import time
import webbrowser
import speech_recognition as sr

#  setting the voice for the assisstant
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)


Assistant_Active = True




# function for Text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



# Function to check Word Present
def word_is_present(word,char):
    if word.find(char)==-1:
        return('not Found')
    else:
        return('present')



# Function to Open THe Driectories through Python Script
def unfold(route):
    os.startfile(route)



# webbrowser Shortfuction
def search(text):
    webbrowser.open_new_tab('https://www.google.com/search?q='+text)





# voice input Function
def voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")

    except Exception :
        speak('sorry Please repeat')
        return"none"
    return(query)








################                        Route              ############################

google = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
cmd = 'C:\\Users\\Rimuru\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk'
vscode = 'C:\\Users\\Rimuru\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
data = 'C:\\Users\\Rimuru\\Desktop\\Data'
anime_dir = 'C:\\Users\\Rimuru\Desktop\\Data\\Anime'
music_dir = 'C:\\Users\\Rimuru\\Desktop\Data\\Music'
filmora = "C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
emulator = ''
git = 'C:\\Program Files\\Git\\git-bash.exe'
settings = 'C:\\Siesta\\Settings.lnk'
vlc = "C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe"
control_pannel = 'C:\\Users\\Rimuru\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk'
playlist_alpha = 'C:\\Siesta\\Alpha_ Music.mp3.xspf'
playlist_beta  = 'C:\\Siesta\\Beta_ Music.mp4.xspf'
playlist_gamma = ''










######    START UP GReet     #####
speak('starting')
speak('system Protocols initiated')
speak('server connection stable')
speak('machine state up and running')
speak('okay sir , everything looks fine')
speak('all systems are initiated without fail')
speak('so sir , what do u need me for ?')













while Assistant_Active:

    ai = voice_command()
    user_input = ai.lower()

    print(user_input)
    #####       THE OPEN COMMANDS        ######

    if 'open' in user_input:
        speak('okay sir')

        print(user_input)
        
        if 'google' in user_input:
            speak('activating google chrome')
            unfold(google)
    
        elif word_is_present(user_input,'cmd')=='present':
            speak('activating cmd')
            unfold(cmd)
        
        elif word_is_present(user_input,'vscode')=='present':
            speak('opennig vs code')
            unfold(vscode)
        
        elif word_is_present(user_input,'code')=='present':
            speak('opennig vs code')
            unfold(vscode)



        elif word_is_present(user_input,'data')=='present':
            speak('accessing data')
            unfold(data)
        
        elif word_is_present(user_input,'anime')=='present':
            speak('opening directory')
            unfold(anime_dir)
        
        elif word_is_present(user_input,'music')=='present':
            speak('locating music directory')
            unfold(music_dir)
        
        elif word_is_present(user_input,'filmora')=='present':
            speak('activating filmora')
            unfold(filmora)
        
        elif word_is_present(user_input,'vlc')=='present':
            speak('firing off vlc')
            unfold(vlc)
        
        elif word_is_present(user_input,'android')=='present':
            unfold(emulator)
        
        elif word_is_present(user_input,'emulator')=='present':
            unfold(emulator)
        
        elif word_is_present(user_input,'git')=='present':
            speak('firing of git bash')
            unfold(git)
        
        elif word_is_present(user_input,'bash')=='present':
            speak('firing of git bash')
            unfold(git)
        
        elif word_is_present(user_input,'setting')=='present':
            speak('opening system settings')
            unfold(settings)
        
        elif word_is_present(user_input,'control pannel')=='present':
            speak('activating control pannel')
            unfold(control_pannel)
        
        elif word_is_present(user_input,'youtube')=='present':
            speak('opening youtube')
            webbrowser.open('https://youtube.com/')
        
        elif word_is_present(user_input,'gmail')=='present':
            speak('accessing gmail account')
            webbrowser.open('https://accounts.google.com/b/0/AddMailService')


       ######     THE FIRE OFF COMMANDS      ######         


    
    elif word_is_present(user_input,'fire off') == 'present':
        
        if word_is_present(user_input,'google')=='present':
            speak('firing off google chrome')
            unfold(google)
        
        elif word_is_present(user_input,'cmd')=='present':
            speak('firing off cmd')
            unfold(cmd)
        
        elif word_is_present(user_input,'vscode')=='present':
            speak('firing off vscode')
            unfold(vscode)
        
        elif word_is_present(user_input,'data')=='present':
            speak('firing off data directory')
            unfold(data)
        
        elif word_is_present(user_input,'anime directory')=='present':
            speak('firing off anime directory')
            unfold(anime_dir)
        
        elif word_is_present(user_input,'music directory')=='present':
            speak('firing off music directory')
            unfold(music_dir)
        
        elif word_is_present(user_input,'filmora')=='present':
            speak('firing off filmora')
            unfold(filmora)
        
        elif word_is_present(user_input,'vlc')=='present':
            speak('firing off vlc')
            unfold(vlc)
        
        elif word_is_present(user_input,'android')=='present':
            speak('emulator')
            unfold(emulator)
        
        elif word_is_present(user_input,'emulator')=='present':
            speak('emulator')
            unfold(emulator)
        
        elif word_is_present(user_input,'git')=='present':
            speak('firing off git bash')
            unfold(git)
        
        elif word_is_present(user_input,'bash')=='present':
            speak('firing off git bash')
            unfold(git)
        
        elif word_is_present(user_input,'setting')=='present':
            speak('firing off settings')
            unfold(settings)
        
        elif word_is_present(user_input,'control pannel')=='present':
            speak('firing off control panel')
            unfold(control_pannel)
        
        elif word_is_present(user_input,'youtube')=='present':
            speak('accessing youtube')
            webbrowser.open('https://youtube.com/')
        
        elif word_is_present(user_input,'gmail')=='present':
            speak('accessing gmail')
            webbrowser.open('https://accounts.google.com/b/0/AddMailService')
    
    
    
            ########   THE PLAY COMMANDS    #######


    elif word_is_present(user_input,'play ')=='present':
    
        if word_is_present(user_input,'music alpha')=='present':
            speak('playing the alpha series playlist')
            unfold(playlist_alpha)
    
        elif word_is_present(user_input,'music beta')=='present':
            speak('playing the beta series playlist')
            unfold(playlist_beta)
     
        elif word_is_present(user_input,'playlist gamma')=='present':
            speak('playlist')
            unfold(playlist_gamma)
    
    
     ########      THE GOOGLE SEARCH COMMAND     #######
    
    elif word_is_present(user_input,'search for')=='present':
        speak('searching')
        index = user_input.find('search for ') + 11
        info = user_input[index::]
        search(info)

     ############    THE INFORMATION SEARCH  COMMAND  ###########

    elif word_is_present(user_input,'about')=='present':
        speak('finding')
        index = user_input.find('about ') + 6
        info = user_input[index::]
        search(info)
    

    ###############          THE YOUTUBE COMMAND         ##############


    elif word_is_present(user_input,'youtube')=='present':
        speak('accessing youtube')
        webbrowser.open('https://youtube.com/')
    

    ############         THE GMAIL COMMAND        #################
    
    elif word_is_present(user_input,'gmail')=='present':
        speak('accessing gamil')
        webbrowser.open('https://accounts.google.com/b/0/AddMailService')


    ############    THE SHUTDOWN OR EXIT COMMANDS
    
    
    elif word_is_present(user_input,'exit')=='present':
        speak('exiting')
        break
    elif word_is_present(user_input,'who are u')=='present':
        speak('sir u programmed me i am siesta')
    elif word_is_present(user_input,'your current version')=='present':
        speak('my current version is 1.0.1')
    elif word_is_present(user_input,'shutdown')=='present':
        speak('shuting down third party')
        break



speak('shutting down the core programme')
speak('shutting down all other servers and system protocols')
speak('if u need something just ask')
speak('have a nice time')

