from weather import Weather, Unit

def weather(intake):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('Riddlesdown')
    condition = location.condition
    print("It is currently "+condition.text)

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
        
        
