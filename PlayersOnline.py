from random import randint
from datetime import datetime
from time import sleep

def printf(text):
    for char in text:
        print(char, end='', flush=True)
        match char:
            case " ":
                sleep(0.1)
            case ",":
                sleep(0.5)
            case ".":
                sleep(1)
            case _:
                sleep(0.05)


playersOnline = randint(0, 10000)
playerPlace = randint(0, playersOnline)
playerPlacePrecent = (playerPlace / playersOnline) * 100

playerPlace = str(playerPlace)
match playerPlace[-1]:
    case "1":
        playerPlace += "st"
    case "2":
        playerPlace += "nd"
    case "3":
        playerPlace += "rd"
    case _:
        playerPlace += "th"
currentHour =  datetime.now().hour
timeGreeting = ""
if currentHour >= 18:
    timeGreeting = "evening"
elif currentHour >= 12:
    timeGreeting = "afternoon"
else:
    timeGreeting = "morning"

printf("Out of the %i players online today, you're in %s place." % (playersOnline, playerPlace))
sleep(1)
printf("\nThat means you're in the top %.0f%% of players today." % (playerPlacePrecent))
sleep(1)
printf("\nHow does that make you feel this " + timeGreeting + "?")
sleep(0.5)
input("\n\tEnter Emotions: ")

sleep(3)