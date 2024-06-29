import os
import time
import random

def health():
  health = ((random.randint(1,6) * random.randint(1,12))/2) + 10
  return health

def strength():
  strength = ((random.randint(1,6) * random.randint(1,12))/2) + 12
  return strength

def die():
  die_roll = random.randint(1,6)
  return die_roll

c1strength = strength()
c1health = health()
c2strength = strength()
c2health = health()

c1name = input("Name your Legend: ")
c1type = input("Character Type (Human, Elf, Wizard, Orc): ")
print("Health:", c1health)
print("Strength:", c1strength)

print("Who are they battling?")

c2name = input("Name your Legend: ")
c2type = input("Character Type (Human, Elf, Wizard, Orc): ")
print("HEALTH: ", c2health)
print("STRENGTH: ", c2strength)

round = 0

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  c1roll = die()
  c2roll = die()
  
  str_diff = abs(c1strength - c2strength) + 1
  if c1health <= 0:
    print(c1name, "has died!")
    print(c2name, "destroyed", c1name, "in", round, "rounds!")
    break
  elif c2health <= 0:
    print(c2name, "has died!")
    print(c1name, "destroyed", c2name, "in", round, "rounds!")
    break
  elif c1roll > c2roll:
    c2health -= str_diff
    round += 1
    print(c1name, "wins round", round)
    print(c2name, "takes a hit, with", str_diff, "damage")
  elif c2roll > c1roll:
    c1health -= str_diff
    round += 1
    print(c2name, "wins round", round)
    print(c1name, "takes a hit, with", str_diff, "damage" )
  else:
    print("The die were tie this round")
    round += 1
    continue