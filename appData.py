# applist for linux os

linuxAppList = {
    'spotify': '/var/lib/snapd/desktop/applications/spotify_spotify.desktop',
    'brave': '/usr/share/applications/brave-browser.desktop',
    'code': '/usr/share/applications/code.desktop',
    'firefox': '/usr/share/applications/firefox.desktop',
    'vlc': '/usr/share/applications/vlc.desktop',
    'obs': '/usr/share/applications/com.obsproject.Studio.desktop',
    'libreoffice': '/usr/share/applications/startcenter.desktop',
    'zoom': '/usr/share/applications/zoom.desktop',
    'pycharm': '/var/lib/snapd/desktop/applications/pycharm-community_pycharm-community.desktop',
    'systemmonitor': '/usr/share/applications/org.kde.ksysguard.desktop',
    'okular': '/usr/share/applications/org.kde.okular.desktop',
    'discord': '/var/lib/snapd/desktop/applications/discord_discord.desktop',
    'terminal': '/usr/share/applications/org.kde.konsole.desktop' 
}

# appList for 
winAppList = {
    'spotify': f'C:\\Users\\Dipanshu\\AppData\\Roaming\\Spotify\\Spotify.exe',
    'discord': f'C:\\Users\\Dipanshu\\AppData\\Local\\Discord\\Update.exe',
    'code': f'C:\\Users\\Dipanshu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'zoom': f'C:\\Users\\Dipanshu\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe',
    'brave': 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe',
    'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'firefox': 'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
    'vlc': 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe',
    'obs': 'C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe',
    'pycharm': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe',
    'adobe reader': 'C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe',
    'excel': 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE', 
    'powerpoint': 'C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\POWERPNT.EXE',
    'access': 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE',
    'word': 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE',
    'outlook': 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE',
    'onedrive': 'C:\\Program Files\\Microsoft OneDrive\\OneDrive.exe',
    'onenote': 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE',
    'publisher': 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSPUB.EXE',
    'microsoft edge': 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    'skype': 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\lync.exe',
    'task manager': '%windir%\\system32\\taskmgr.exe',
    'terminal': '%windir%\\system32\\cmd.exe'
}

def checkWinAppDict(winAppList ,query):
    for app in winAppList:
        if app in query: 
            return app

def checkLinuxAppDict(linuxAppList ,query):
    for app in winAppList:
        if app in query: 
            return app