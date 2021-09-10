# GameEvents.py

from Profile import *
from Extensions import *

profile = Profile()

def welcome():
	print("Welcome to the Grand Canyon Mountain Adventure Game")
	print("*********************************************")
	print("You are visiting the Grand Canyon.")
	print("You go on a hike alone on the Hermit trail.  This trail has washouts and rockslides and requires some navigating skills to find the routes.")
	spacer()

def userChooseItem():
	choice = input("Choose an item: map(m), flashlight(f), chocolate(c), rope(r), or stick(s)").lower()

	while checkIfUserInputIsValid(choice, ["m", "f", "c", "r", "s"]) == False:
		choice = input("Choose an item: map(m), flashlight(f), chocolate(c), rope(r), or stick(s)")

	profile.item = choice
	print("You chose a", profile.possibleItems[choice])
	spacer()

def checkIfUserInputIsValid(userChoice, possibleChoices):
	return userChoice in possibleChoices


def hearASound():
	print("You hear a humming sound.")
	choice = input("Do you want to follow it? (y/n)").lower()

	while checkIfUserInputIsValid(choice, ["y", "n"]) == False:
		choice = input("Do you want to follow it? (y/n)")

	profile.hummingSound = choice

	if choice == "y":
		followSound()
	else:
		chooseLost()

def followSound():
	spacer()
	print("You keep moving closer to the sound.")
	print("The sound suddenly stops")
	print("You are now LOST!")
	print("You try to call on your phone but there is no signal!")

def chooseLost():
	print("You start walking back to the starting point.")
	print("You realize that you are LOST!")
	print("The sound is behind you and is getting louder. You panic!")

def lost():
	spacer()
	choice = input("do you want to run (r) or make a call (c)?").lower()
	userChoseCall = True

	while checkIfUserInputIsValid(choice, ["r", "c"]) == False and userChoseCall == True:
		choice = input("do you want to run (r) or make a call (c)?").lower()

	if choice == "c":
		print("The call did not go through")
		lost()
		return

	print("You start running really fast")
	print("The sounds gets louder")

def direction():
	spacer()
	userDirection = input("Which direction will you run?: north, west, south, or highway").lower()

	while checkIfUserInputIsValid(userDirection, ["north", "west", "south", "highway"]) == False:
		userDirection = input("Which direction will you run?: north, west, south, or highway").lower()

	profile.direction = userDirection

	spacer()
	eval(userDirection+"()")

def north():
	print("You start running north")
	print("You reach the cabin and realize you are lost.")

	if profile.item == "m":
		print("Since you have a map, you use that to find your way out of The Grand Canyon Mountain")
		profile.gameState = "won"
		destructiveMessage("YOU WIN! GOOD BOY")
	else:
		print("Since you don't have a map, you cannot find your way out of The Grand Canyon Mountain")
		destructiveMessage("YOU LOST!")
		profile.gameState = "lost"

def west():
	print("You start running from the sound")
	print("Oh NO! You hurt your leg!")
	destructiveMessage("YOU LOST!")
	profile.gameState = "lost"

def south():
	## Reach the bridge
	print("You start running south from the sound")
	print("You run into a bridge and find need a tool")
	bridge()

def highway():
	print("You decide that none of the cardinal directions sound great and run for the highway")
	print("Unfortunately, it is too dark for you to see")
	bridge()

def bridge():
	if profile.item == "r" or profile.item == "s":
		print("Because you have a tool (Rope or Stick), you fix the bridge and find your way out of The Grand Canyon Mountain")
		profile.gameState = "won"
		destructiveMessage("YOU WIN! GOOD BOY")
	else:
		print("Sadly, you do not have a tool to fix the bridge (Rope or Stick) and cannot find your way out of The Grand Canyon Mountain")
		profile.gameState = "lost"
		destructiveMessage("YOU LOST!")


def logProfileDetails():
	spacer()
	print("User Profile Details")
	print("*********************************************")
	spacer()

	print("User chosen item =", profile.item)
	print("Possible items chosen =", profile.possibleItems)
	print("Humming sound decision =", profile.hummingSound)
	print("User direction =", profile.direction)
	print("Game state =", profile.gameState)