import karen.app
import sys


def main(args):
    for arg in args:
        karen.app.tests(arg)


if __name__ == "__main__":
    main(sys.argv[1:])
