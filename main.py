import PySimpleGUI as sg
import os
import yt_dlp
import asyncio
import sys
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch

sg.ChangeLookAndFeel('DarkPurple')
working_directory = os.getcwd()
tipolink = ''
estado = 0
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id="CLIENT ID GOES HERE",
                                                                     client_secret="SECRET ID GOES HERE")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# Define the window's contents
layout = [
    [sg.Image(filename='logocopy.png', size=(200, 40), pad=(0, 0)),
     sg.Text('v1.2.2', size=(29, 1), pad=(2, 0), font=('Any 10')), sg.Button('Help', pad=(2, 0))],
    [sg.Text("URL:         ", font=('Any 10 bold'), pad=(2, 0)), sg.Input(key='LINK')],
    [sg.Text("Output:     ", font=('Any 10 bold'), pad=(2, 0)), sg.InputText(key='FOLDER'),
     sg.FolderBrowse(initial_folder=working_directory, target='FOLDER')],
    [sg.Text('Link:', size=(64, 1), key='ESTADOL', pad=(2, 0))],
    [sg.Text('Source:', size=(60, 1), key='ESTADOT', pad=(2, 0))],
    [sg.Text('Output:', size=(60, 1), key='ESTADOF', pad=(2, 0))],
    [sg.Text('Waiting...', size=(60, 1), key='ESTADO', font=('Any 12 bold'), pad=(2, 0))],
    [sg.Button('Verify', pad=(4, 0)), sg.Button('Download', pad=(4, 0)), sg.Button('Quit', pad=(4, 0)),
     sg.Text('Maximo Ospital, 2022.', size=(62, 1), pad=(2, 0), justification='right', font=('Any 10'))]
]

# Create the window
window = sg.Window('cheatjockey v1.2.2', layout, size=(500, 215), margins=(5, 5))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    elif event == 'Help':
        sg.popup(
            'Paste the link (Spotify, Youtube, Bandcamp and Soundcloud supported) and the output directory in their respective form fields, and press Verify and afterwards Download.')
    elif event == 'Verify':
        LINK = values['LINK']
        window['ESTADO'].update('  Verifying...')
        window.Refresh()
        if LINK.find("https://open.spotify.com/playlist/") != -1 or LINK.find(
                "http://open.spotify.com/playlist/") != -1 or LINK.find(
            "https://www.open.spotify.com/playlist/") != -1 or LINK.find(
            "http://www.open.spotify.com/playlist/") != -1:
            tipolink = 'Spotify playlist'
            playlist_URI = LINK.split("/")[-1].split("?")[0]
            track_name = [x["track"]["name"] for x in sp.playlist_items(playlist_URI)["items"]]
            track_artist = [x["track"]["artists"][0]["name"] for x in sp.playlist_items(playlist_URI)["items"]]
            playlist = sp.playlist_items(playlist_URI, fields='items.track.artists.name,items.track.name')
            canciones = []
            for x in range(len(track_name)):
                cancion = (track_artist[x] + ' - ' + track_name[
                    x] + ' "Auto-generated by YouTube."')
                canciones.append(cancion)
            for word in canciones:
                    result = word.encode('utf-8')
        elif LINK.find("https://open.spotify.com/album/") != -1 or LINK.find(
                "http://open.spotify.com/album/") != -1 or LINK.find(
            "https://www.open.spotify.com/album/") != -1 or LINK.find(
            "http://www.open.spotify.com/album/") != -1:
            tipolink = 'Spotify album'
            album_URI = LINK.split("/")[-1].split("?")[0]
            album_tracks = sp.album_tracks(album_URI)
            print(album_tracks)
            track_name = [x["name"] for x in album_tracks["items"]]
            track_artist = [x["artists"][0]["name"] for x in album_tracks["items"]]
            track_number = [x["track_number"] for x in album_tracks["items"]]
            album = sp.album_tracks(album_URI)
            canciones = []
            for x in range(len(track_name)):
                cancion = (track_artist[x] + ' - ' + track_name[
                    x] + ' "Auto-generated by YouTube."')
                canciones.append(cancion)
            for word in canciones:
                    result = word.encode('utf-8')
                    print(result)
        elif LINK.find("https://open.spotify.com/track/") != -1 or LINK.find(
                "http://open.spotify.com/track/") != -1 or LINK.find(
            "https://www.open.spotify.com/track/") != -1 or LINK.find(
            "http://www.open.spotify.com/track/") != -1:
            tipolink = 'Spotify track'
            track_URI = LINK.split("/")[-1].split("?")[0]
            track = sp.track(track_URI)
            print(track)
            track_name = track["name"]
            track_artist = track["artists"][0]["name"]
            cancion = (track_artist + ' - ' + track_name + ' "Auto-generated by YouTube."')
            print(cancion)
        elif LINK.find("youtube.com") != -1:
            tipolink = 'YouTube'
        elif LINK.find("soundcloud.com") != -1:
            tipolink = 'SoundCloud'
        elif LINK.find("bandcamp.com") != -1:
            tipolink = 'Bandcamp'
        else:
            tipolink = 'No valido'
        window['ESTADOL'].update('Link: ' + values['LINK'])
        window['ESTADOT'].update('Source: ' + tipolink)
        window['ESTADOF'].update('Output: ' + values['FOLDER'])
        if not values['LINK']:
            print('Link vacio')
            window['ESTADO'].update('Empty link.')
            estado = 0
        if not values['FOLDER']:
            print('Directorio vacio')
            window['ESTADO'].update('Please choose a folder.')
            estado = 0
        if values['LINK'] and tipolink == "No valido":
            window['ESTADO'].update('Invalid link')
            estado = 0
        if not values['LINK'] and not values['FOLDER']:
            window['ESTADO'].update('Empty link and no folder selected.')
        if values['LINK'] and tipolink != "No Valido" and values['FOLDER']:
            window['ESTADO'].update(tipolink + ' url and valid output folder.')
            estado = 1
    elif event == 'Download' and estado == 0:
        window['ESTADO'].update('Please verify before downloading.')
        window.Refresh()
    elif event == 'Download' and estado == 1:
        window['ESTADO'].update("Downloading... (Not stuck, don't worry)")
        window.Refresh()
        if tipolink == 'YouTube' or tipolink == 'SoundCloud' or tipolink == 'Bandcamp':
            logname = 'log-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
            if 'playlist' in values['LINK']:
                archivonombre = '/%(playlist_index)s.%(uploader)s - %(title)s.%(ext)s'
            else :
                archivonombre = '/%(uploader)s - %(title)s.%(ext)s'
            sys.stdout = open(logname, "w")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': values['FOLDER'] + archivonombre,
                'postprocessors': [
                    {  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                    },
                    {
                        'key': 'FFmpegMetadata'
                    }
                ]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(values['LINK'])
                window['ESTADO'].update('Done!')
                os.startfile(values['FOLDER'])
                estado == 0
                sys.stdout.close()
        elif tipolink == 'Spotify track':
            logname = 'log-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
            sys.stdout = open(logname, "w")
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': values['FOLDER'] + '/%(uploader)s - %(title)s.%(ext)s',
                'postprocessors': [
                    {  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                    },
                    {
                        'key': 'FFmpegMetadata'
                    }
                ]
            }
            videosSearch = VideosSearch(cancion, limit=1)
            videosResult = videosSearch.result()['result'][0]['link']
            print(videosResult)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(videosResult)
            for filename in os.listdir(values['FOLDER']):
                if '- Topic' in filename:
                    filepath = os.path.join(values['FOLDER'], filename)
                    newfilepath = os.path.join(values['FOLDER'], filename.replace('- Topic', ""))
                    try:
                        os.rename(filepath, newfilepath)
                    except WindowsError:
                        os.remove(newfilepath)
                        os.rename(filepath, newfilepath)
            window['ESTADO'].update('Done!')
            os.startfile(values['FOLDER'])
            estado == 0
            sys.stdout.close()
        elif tipolink == 'Spotify playlist' or tipolink == 'Spotify album':
            logname = 'log-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
            sys.stdout = open(logname, "w")
            for x in range(len(canciones)):
                if 'playlist' or 'album' in values['LINK']:
                    archivonombre = '/'+str(x+1)+'.%(uploader)s - %(title)s.%(ext)s'
                else:
                    archivonombre = '/%(uploader)s - %(title)s.%(ext)s'
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': values['FOLDER'] + archivonombre,
                    'postprocessors': [
                        {  # Extract audio using ffmpeg
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '320',
                        },
                        {
                            'key': 'FFmpegMetadata'
                        }
                    ]
                }
                print(canciones[x].encode("utf-8"))
                videosSearch = VideosSearch(canciones[x], limit=1)
                videosResult = videosSearch.result()['result'][0]['link']
                print(videosResult)
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(videosResult)
                for filename in os.listdir(values['FOLDER']):
                    if '- Topic' in filename:
                        filepath = os.path.join(values['FOLDER'], filename)
                        newfilepath = os.path.join(values['FOLDER'], filename.replace('- Topic', ""))
                        try:
                            os.rename(filepath, newfilepath)
                        except WindowsError:
                            os.remove(newfilepath)
                            os.rename(filepath, newfilepath)
            window['ESTADO'].update('Done!')
            os.startfile(values['FOLDER'])
            estado == 0
            sys.stdout.close()
# Finish up by removing from the screen
window.close()
