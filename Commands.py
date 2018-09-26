#! /usr/bin/env python3

from weather import Weather, Unit
import random
import datetime
import time
import pygame


def weather(intake):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('Riddlesdown')
    condition = location.condition
    print("It is currently "+condition.text)

def Science():
    Question = input("What makes up everything?")
    if Question == "atoms":
        print("Correct!")
    else:
        print("Incorrect...")

def Maths():
    Ask = input("What level would you like : Easy, Intermediate, Expert?")
    if Ask == "easy":
        Number1 = random.randint(1,10)
        Number2 = random.randint(1,10)
        Question = input("What's "+str(Number1)+" + "+str(Number2)+"?")
        if Question == str(Number1+Number2):
            print("Correct!")
        else:
            print("Incorrect...")
    if Ask == "intermediate":
        Number1 = random.randint(1,100)
        Number2 = random.randint(1,100)
        Choice = random.randint(1,2)
        if Choice == 1:
            Question = input("What's "+str(Number1)+" + "+str(Number2)+"?")
            if Question == str(Number1+Number2):
                print("Correct!")
            else:
                print("Incorrect...")
        if Choice == 2:
            Question = input("What's "+str(Number1)+" - "+str(Number2)+"?")
            if Question == str(Number1-Number2):
                print("Correct!")
            else:
                print("Incorrect...")
    if Ask == "expert":
        Number1 = random.randint(1,1000)
        Number2 = random.randint(1,1000)
        Choice = random.randint(1,4)
        if Choice == 1:
            Question = input("What's "+str(Number1)+" + "+str(Number2)+"?")
            if Question == str(Number1+Number2):
                print("Correct!")
            else:
                print("Incorrect...")
        if Choice == 2:
            Question = input("What's "+str(Number1)+" - "+str(Number2)+"?")
            if Question == str(Number1-Number2):
                print("Correct!")
            else:
                print("Incorrect...")
        if Choice == 3:
             Question = input("What's "+str(Number1)+" / "+str(Number2)+"?")
             if Question == str(Number1/Number2):
                 print("Correct!")
             else:
                 print("Incorrect...")           
        if Choice == 4:
              Question = input("What's "+str(Number1)+" X "+str(Number2)+"?")
              if Question == str(Number1*Number2):
                  print("Correct!")
              else:
                  print("Incorrect...")

def English():
    Question = input("What language is used when using metaphorical or symbolic phrases/words?")
    if Question == 'figurative':
        print("Correct!")
    else:
        print("Incorrect...")

def History():
    Question = input("What machine was used by the Germans in WW1 to encrypt messages?")
    if Question == 'enigma machine':
        print("Correct!")
    else:
        print("Incorrect...")

def Geography():
    Question = input("In which continent is Alabama?")
    if Question == 'north america':
        print("Correct!")
    else:
        print("Incorrect...")

def CalAdd(intake):
    Numbers = [int(input("1st number = ")), int(input("2nd number = "))]
    print(Numbers[0] + Numbers[1])

def CalSub(intake):
    Numbers = [int(input("1st number = ")), int(input("2nd number = "))]
    print(Numbers[0] - Numbers[1])

def CalDiv(intake):
    Numbers = [int(input("1st number = ")), int(input("2nd number = "))]
    print(Numbers[0] / Numbers[1])

def CalMul(intake):
    Numbers = [int(input("1st number = ")), int(input("2nd number = "))]
    print(Numbers[0] * Numbers[1])

def Game():
    choice = random.randint(1,5)
    if choice == 1:
        Science()
    if choice == 2:
        Maths()
    if choice == 3:
        English()
    if choice == 4:
        History()
    if choice == 5:
        Geography()

def Time():
    day = datetime.datetime.now()
    print(day)

def Timer():
    Unit = input("What units will you use (seconds, minutes or hours)?")
    if Unit == 'seconds':
        Amount = input("How long are you timing for?")
        time.sleep(int(Amount))
        print("Times up!!!!!!!!")
    if Unit == 'minutes':
        Amount = input("How long are you timing for?")
        Amount = int(Amount) * 60
        time.sleep(int(Amount))
        print("Times up!!!!!!!!")
    if Unit == 'hours':
        Amount = input("How long are you timing for?")
        Amount = int(Amount) * 60
        Amount = int(Amount) * 60
        time.sleep(int(Amount))
        print("Times up!!!!!!!!")

def Music():
    music = input("Enter the name of the song and the type of file(.ogg)")
    pygame.init()
    song = pygame.mixer.Sound(music)
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()
