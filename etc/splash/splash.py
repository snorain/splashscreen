import vlc
import time

#Defince startup video
startup = vlc.Media("/etc/splash/splash.mp4")

#Define volume
volume = 45

#Create splashscreenplayer
media_player = vlc.MediaPlayer()

#Set splashscreen
media_player.set_media(startup)

#Set volume
media_player.audio_set_volume(volume)

#Play splashscreen
media_player.play()
time.sleep(4)
print("End")
media_player.stop()
