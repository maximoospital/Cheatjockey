
# ![Logo](https://i.imgur.com/Ox9eYbt.png)

This app converts Spotify, SoundCloud and YouTube playlists to MP3s of the highest possible quality ( without recurring to illegal sources, of course ;) ).

This app does not decode files downloaded by Spotify nor does it use its API for piracy, it purely reads playlists through it.

## Features

- Downloads songs in playlists from:
    - Spotify
    - SoundCloud
    - YouTube
- Log window gives real-time update of the process
- Made with the objective of being a resource-efficient and minimal app, scripted in Python.


## Screenshots

![App Screenshot](https://i.imgur.com/Hw6Qf9E.png)

![App Screenshot](https://i.imgur.com/1OlvAay.png)


## Libraries used

 - [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
 - [YT-DLP (Youtube-DL fork)](https://github.com/yt-dlp/yt-dlp)
 - [Youtube Search Python](https://github.com/alexmercerind/youtube-search-python)
 - [SpotiPy](https://github.com/plamere/spotipy)
 - [PyInstaller (Only used in the pre-compiled verison)](https://github.com/pyinstaller/pyinstaller)

## Manual build

This program is only available as a compiled binary for Windows, however, if you want to build your own Linux or Mac version, you can go ahead and compile it yourself, or just run the source code.

Keep in mind this was coded in Python 3.9.10, so it might not work well under older versions (May god help you if you're still on Python 2.6)

#### If you plan on reading Spotify playlists, it is important that you get a [Spotify Developer](https://developer.spotify.com/) account and get your own App client id and secret id codes, since the source code does not include these for privacy reasons.

Clone the project

```bash
  git clone https://github.com/maximoospital/Cheatjockey.git
```

Go to the project directory

```bash
  cd Cheatjockey
```

Install requirements

```bash
  pip install -r requirements.txt
```
OPTIONAL: If you want Spotify functionality, modify the next line (line number 14) to include the codes you copied earlier.

```bash
  client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id="Client ID goes here", client_secret="Client Secret goes here")
```
Run app

```bash
  python main.py
```

### Linux and other operating systems (Builds ≤ 1.1)

Since this app was built quickly and mainly for my Windows computer, it utilizes certain shortcuts that work perfectly in Windows 10, but not might work as well in other OSes; 
Mainly, lines 114, 129 and 154 of main.py, which contain this command to open the output folder.

```bash
  os.startfile(values['FOLDER'])
```
Which, while perfectly working in Windows, i've read it might be buggy in Linux and other operating systems. I'll change it on the next update, of course, but for now that's something to consider when trying to use your own manually compiled build.


Something else i haven't tested yet is the lack of FFMPEG executables, or rather, the lack of FFMPEG executables not made for Windows. The compiled Windows build already includes these, but it can also work with Environment Variable paths for these.

[![Logo](https://i.imgur.com/XlF4lM5.png)](https://github.com/maximoospital) 
