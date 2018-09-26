#! /usr/bin/env python3

from weather import Weather, Unit
import Commands

intake = str(input(""))

Calculator = ['calculator addition', 'calculator subtraction', 'calculator division' , 'calculator multiplication']
Inputs = ['what is the weather like?', 'game' ,'what is the time?', 'set timer']

if intake == Inputs[0]:
    Commands.weather(intake)
if intake == Calculator[0]:
    Commands.CalAdd(intake)
if intake == Calculator[1]:
    Commands.CalSub(intake)
if intake == Calculator[2]:
    Commands.CalDiv(intake)
if intake == Calculator[3]:
    Commands.CalMul(intake)
if intake == Inputs[1]:
    Commands.Game()
if intake == Inputs[2]:
    Commands.Time()
if intake == Inputs[3]:
    Commands.Timer()

