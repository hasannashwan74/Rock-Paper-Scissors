from random import randint 
import time
playerscore = 0
computerscore= 0

list = ["Rock", "Paper", "Scissors"]
computer=list[randint(0,2)]
player = False

while player == False:
  player = input("Rock, Paper, Scissors?")
  if player == computer:
    print("Tie!")
  elif player == "Rock":
    if computer == "Paper":
      print("computer choses", computer)
      time.sleep(2)
      print("you lose!", computer, "covers", player)
      computerscore=+1
    else:
      print("computer choses", computer)
      time.sleep(2)
      print("you win!", player, "smashes", computer)
      playerscore=+1
  elif player == "Paper":
    if computer == "Scissors":
      print("computer choses", computer)
      time.sleep(2)
      print("you lose!", computer, "cut", player)
      computerscore=+1
    else:
      print("computer choses", computer)
      time.sleep(2)
      print("you win!", player, "covers", computer)
      playerscore=+1
  elif player == "Scissors":
    if computer == "Rock":
      print(" computer choses", computer)
      time.sleep(2)
      print("you lose!", computer, "smashes", player)
      computerscore=+1
    else:
      print("computer choses", computer)
      time.sleep(2)
      print("you win!", player, "cuts", computer)
      playerscore=+1
  else:
    print("that's not your valid play. check you spelling!")
    
print (computerscore)
print (playerscore)
player = False
computer=list[randint(0,2)]