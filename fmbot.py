import pylast
import time

# Your Last.fm API key and secret
API_KEY = "edeed42a078b0b4a552ba4ab26efb6fe"
API_SECRET = "0db7c21440d0862148c9ba03ff78134f"

# Get Information
username = input("Username : ")
password = input("Password: ")
artist = input("Artist Name : ")
title = input("Song Title : ")
loop_delay = input("Loop Delay : ")
password_hash = pylast.md5(password)

# Last.fm 
lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                              username=username, password_hash=password_hash)

count = 0;


while True:
    try:
        # Scrobble verisini gönderin
        lastfm.scrobble(artist=artist, title=title, timestamp=int(time.time()))
        count +=1
        # Başarılı bir şekilde gönderildiğini doğrulayın
        print(f"Successfully sent! ({count})")
    except pylast.WSError as e:
        # Hata alındıysa hata mesajını yazdırın ve döngüyü devam ettirin
        print("Hata:", e)

    # Döngüyü belirtilen süreyle bekletin
    time.sleep(float(loop_delay))
