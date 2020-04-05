import karen
import os

# TODO: receive hardcoded puredata psend port
PSENDPORT = 3000


def pdsend(message=""):
    try:
        os.system("echo '" + message + ";' | pdsend " + str(PSENDPORT))
    finally:
        pass


def audioonoff(play):
    if play is True:
        pdsend("audioonoff 1")
    else:
        pdsend("audioonoff 0")


def audiovolume(volume):
    if volume <= 80:
        pdsend("audiovolume " + str(volume))
    else:
        pdsend("audiovolume 80")


def printvalues(values: str):
    for line in values.splitlines(True):
        pdsend("printvalues " + line)