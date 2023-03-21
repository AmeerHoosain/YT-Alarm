import pafy
import vlc
from alarm import countdown, get_sec
from time import *


def play_song(url):
    is_opening = False
    is_playing = False

    video = pafy.new(url)
    best = video.getbestaudio()
    play_url = best.url

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(play_url)
    media.get_mrl()

    time_sec = countdown()
    if "yes" in countdown():
        timeSec = get_sec(str(time_sec))
        for x in range(timeSec, 0, -1):
            sec = x % 60
            min = int(x / 60) % 60
            hr = int(x / 3600)
            print(f"{hr:02}:{min:02}:{sec:02}")
            sleep(1)

    player.set_media(media)


    player.play()

    good_states = [
        "State.Playing",
        "State.NothingSpecial",
        "State.Opening"
    ]

    while str(player.get_state()) in good_states:
        if str(player.get_state()) == "State.Opening" and is_opening is False:
            print("Status: Loading")
            is_opening = True

        if str(player.get_state()) == "State.Playing" and is_playing is False:
            print("Status: Playing")
            is_playing = True

    print("Status: Finish")
    player.stop()
