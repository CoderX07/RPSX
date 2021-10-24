import random
from art import *

botOptions = ["Rock", "Paper", "Scissors"]

RPS = {
  "R" : "Rock",
  "P" : "Paper",
  "S" : "Scissors"
}

DWS = {
  "Wins" : 0,
  "Draws" : 0,
  "Loses" : 0
}

tprint("RPSX")

def lose():
  print("You Lost 😔")
  DWS["Loses"] += 1
  for key,value in DWS.items():
    print(key, ":", value)

def win():
  print("You Won 😃")
  DWS["Wins"] += 1
  for key,value in DWS.items():
    print(key, ":", value)

while(True):
  botChoice = random.choice(botOptions)
  userInput = input("Rock (R), Paper (P), Scissors (S), Or Random (D)? ")
  userInput = userInput.upper()
  if (userInput == "D"):
    userInput = random.choice(botOptions)
    print()
    print(f"User Choice: {userInput}")
    print(f"Bot Choice: {botChoice}")
    print()
  else:
    if userInput in RPS:
      userInput = RPS[userInput]
      print()
      print(f"User Choice: {userInput}")
      print(f"Bot Choice: {botChoice}")
      print()
    else:
      break
  
  if (userInput == botChoice):
    print("It's A Draw 🤷‍")
    DWS["Draws"] += 1
    for key,value in DWS.items():
      print(key, ":", value)
  else:
    if (userInput == "Rock" and botChoice == "Paper"):
      lose()
    elif (userInput == "Paper" and botChoice == "Scissors"):
      lose()
    elif (userInput == "Scissors" and botChoice == "Rock"):
      lose()
    elif (userInput == "Paper" and botChoice == "Rock"):
      win()
    elif (userInput == "Scissors" and botChoice == "Paper"):
      win()
    elif (userInput == "Rock" and botChoice == "Scissors"):
      win()

  print()
  print("\n---------------------------------\n")
  print()