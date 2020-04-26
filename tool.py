import time
import webbrowser

WORK_INTERVAL = 50  # in minutes
BREAK_INTERVAL = 9  # in minutes

WORK_MUSIC = "https://youtu.be/_ImFiU0G_08"
BREAK_MUSIC = "https://youtu.be/daHQY0cBpEQ"

WORKING = 0
BREAKING = 1


def main():
    current_session = WORKING
    while True:
        if current_session == WORKING:
            print("Working for {} minutes...".format(WORK_INTERVAL))
            do(WORK_MUSIC, WORK_INTERVAL)
        else :
            print("Breaking for {} minutes...".format(BREAK_INTERVAL))
            do(BREAK_MUSIC, BREAK_INTERVAL)
        current_session = 1 - current_session


def do(start_music_url, interval):
    webbrowser.open(start_music_url)
    time.sleep((interval * 60))


if __name__ == "__main__":
    main()
