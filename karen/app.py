import karen.polling as polling
import karen.pd as pd
import selfspy


BACK = ['1', 'w']
ACTIVE_SECONDS = 180

# lines can't contain commas.
# Else PD will treat the list as a concatenation of messages
VALUES = "255 keystrokes in 46 key sequences 189 clicks (164 excluding scroll) 17823 mouse movements \n\
Total time active: 0 days 0h 0m 0s \n\
\n\
Keys / Clicks: 1.3\n\
Active seconds / Keys: 10.9\n\
\n\
Mouse movements / Keys: 69.9\n\
Mouse movements / Clicks: 94.3\n\
\n\
255 keystrokes in 46 key sequences 189 clicks (164 excluding scroll) 17823 mouse movements\n\
\n\
Total time active: 0 days 0h 0m 0s\n\
\n\
Keys / Clicks: 1.3\n\
Active seconds / Keys: 10.9\n\
\n\
Mouse movements / Keys: 69.9\n\
Mouse movements / Clicks: 94.3"


def tests(args):
    if args == "polling":
        polling.ratios(ACTIVE_SECONDS, BACK)
    if args == "pd":
        pd.printvalues(VALUES)
    if args == "start-selfspy":
        selfspy.main()
