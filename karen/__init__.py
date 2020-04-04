import os

# TODO: receive hardcoded puredata psend port
PSENDPORT = 3000


def psend(message=""):
    try:
        os.system("echo '" + message + ";' | pdsend " + str(PSENDPORT))
    finally:
        pass


def audioonoff(play):
    if play is True:
        psend("audioonoff 1")
    else:
        psend("audioonoff 0")


def audiovolume(volume):
    if volume <= 80:
        psend("audiovolume " + str(volume))
    else:
        psend("audiovolume 80")