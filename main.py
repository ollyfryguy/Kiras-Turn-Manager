import random
import shutil
import sys
import textwrap
import time

amountOfStandardActions = 1
amountOfSwiftActions = 1
amountOfMovementActions = 1
loopManager = True
actionUsed = ""
chausableOfFellPower = True
testVariable = True
glovesOfEldritchAdmixtureCharges = 3
glovesOfEldritchAdmixture2d6 = False
glovesOfEldritchAdmixture3d6 = False
glovesOfEldritchAdmixture4d6 = False
playerDexMod = 6
print("Welcome to Kira's Turn Manager! Ready to make your move?")
def amountOfActions():
  print("You have " + str(amountOfStandardActions) + " standard actions remaining.")
  print("You have " + str(amountOfSwiftActions) + " swift actions remaining.")
  print("You have " + str(amountOfMovementActions) + " movement actions remaining.")


def rollDiceD6():
  return random.randint(1, 6)
def rollDiceD4():
  return random.randint(1, 4)
def rollDiceD8():
  return random.randint(1, 8)
def rollDiceD10():
  return random.randint(1, 10)
def rollDiceD12():
  return random.randint(1, 12)
def rollDiceD20():
  return random.randint(1, 20)
def rollDiceD100():
  return random.randint(1, 100)


def multipleD6s(n):
  damageCalc = []
  for _ in range(n):
    damageCalc.append(rollDiceD6())
  total = sum(damageCalc)
  damageCalc = total
  return damageCalc

def eldritchBlast(n):
  damageCalc = []
  for _ in range(n):
    damageCalc.append(rollDiceD6())
  total = sum(damageCalc)
  damageCalc = total
  return damageCalc


def delayPrint(t):
  #Im not exactly sure why this is working. It sets the variable message as itself with added formatting to not cut off words. 
  global message
  message = textwrap.fill(message, width=shutil.get_terminal_size().columns)
  #Then for each Character (c) in the newly set message, it runs the loop below.
  for c in message:
    #It writes the character
    sys.stdout.write(c)
    sys.stdout.flush()
    #Then waits for the time put.
    time.sleep(t)
    
print(1  + 1)
while loopManager is True:
  message = ("\nPlease Input your move. Type 'Actions Remaining' to see your remaining actions and 'reset' to reset your amount of actions. \n \n")
  delayPrint(0.02)
  print("\n")
  actionUsed = str.casefold(input(""))
  if actionUsed == ("actions remaining"):
    amountOfActions()

  if actionUsed == ("eldritch blast") and amountOfStandardActions >= 1 or actionUsed == ("eb") and amountOfStandardActions >= 1:
    #This is for regular eldritch blast— not eldritch claw.
    rolledD20 = rollDiceD20()
    if rolledD20 == 20:
      print("Rolled Nat 20")
    rolledAttack = rolledD20 + playerDexMod + 11 + 1
    print(rolledAttack)
    amountOfStandardActions = amountOfStandardActions - 1
    amountOfActions()

    #Convert rolledAttack to string
    rolledAttackStr = str(rolledAttack)
    
    print("Did " + rolledAttackStr + " hit?")
    attackOverAC = str.casefold(input(""))
    if attackOverAC == ("yes"):
      DamageTotalEB = eldritchBlast(7)
      if chausableOfFellPower is True:
        DamageTotalEB = DamageTotalEB + multipleD6s(2)

      if glovesOfEldritchAdmixture2d6 is True:
        DamageTotalEB = DamageTotalEB + multipleD6s(2)
        glovesOfEldritchAdmixture3d6 = False
      
      if glovesOfEldritchAdmixture3d6 is True:
        DamageTotalEB = DamageTotalEB + multipleD6s(3)

      if glovesOfEldritchAdmixture4d6 is True:
        DamageTotalEB = DamageTotalEB + multipleD6s(4)

      #Converts DamageTotalEB to string
      DamageTotalEBStr = str(DamageTotalEB)

      print(DamageTotalEBStr + " Damage dealt.")
    elif attackOverAC == ("no"):
      continue
    else:
      message = ("Not a valid input")
      delayPrint(0.03)
      print("\n")
     


  if actionUsed == ("reset"):
    amountOfStandardActions = 1
    amountOfSwiftActions = 1
    amountOfMovementActions = 1
    glovesOfEldritchAdmixture2d6 = False
    glovesOfEldritchAdmixture3d6 = False
    glovesOfEldritchAdmixture4d6 = False
    amountOfActions()
    

#For future reference, from the official srd (https://www.dandwiki.com/wiki/SRD:Natural_Weapons), "Creatures do not receive additional attacks from a high base attack bonus when using natural weapons."
