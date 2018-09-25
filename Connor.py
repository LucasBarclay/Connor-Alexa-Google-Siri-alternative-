from weather import Weather, Unit
import Commands

intake = str(input(""))

Calculator = ['calculator addition', 'calculator subtraction', 'calculator division' , 'calculator multiplication']
Wh = 'what is the weather like?'
Game = 'game'
Time = 'what is the time?'
Timer = 'set timer'

if intake == Wh:
    Commands.weather(intake)
if intake == Calculator[0]:
    Commands.CalAdd(intake)
if intake == Calculator[1]:
    Commands.CalSub(intake)
if intake == Calculator[2]:
    Commands.CalDiv(intake)
if intake == Calculator[3]:
    Commands.CalMul(intake)
if intake == Game:
    Commands.Game()
if intake == Time:
    Commands.Time()
if intake == Timer:
    Commands.Timer()

