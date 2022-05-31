# This program simulates Conway's game of life 
# Programmed by Will Caron

# RULES
# 1.) Any live cell with less than 2 neighbors dies as if by underpopulation
# 2.) Any live cell with 2-3 neighbors lives on to the next generation 
# 3.) Any live cell with more than 3 neighbors dies as if by overpopulation

# Good luck!

# Imports
from os import get_terminal_size, system
from time import sleep
from random import randint

# Function definitions

# Clears the terminal window
def clear():
  system('clear')

# Gets the size of the terminal window
def size():
  # Lines, Columns
  terminalSize = [get_terminal_size()[1], get_terminal_size()[0]]
  return terminalSize

# generates a feild to play on
def generateField(typeE = " "):
  dimensions = size()
  field = []
  for row in range(dimensions[0]):
    field.append([])
    for column in range(dimensions[1]):
      field[row].append(typeE)
  return field

# formats for and prints the feild in the terminal
def showField(feild):
  for rows in range(len(feild)):
    for columns in range(len(feild[0])):
      print(feild[rows][columns], sep="", end="")
    print()

# adds live cells to the feild
def add(feild, typed = "#"):
  screen = size()
  number = int(input("Enter amount of live pixels to add: "))
  while number < 0 or number > (screen[0]*screen[1]):
    number = int(input("Enter amount of live pixels to add: "))
  for i in range(number):
    x = int(input("Enter X coordinate to add (1 to "+str(screen[1])+"): "))-1
    while x < 0 or x > screen[1]:
      x = int(input("Invalid. Enter X coordinate to add (1 to "+str(screen[1])+"): "))-1
    y = int(input("Enter Y coodinate to add (1 to "+str(screen[0])+"): ")) - 1
    while y < 0 or y > screen[0]:
      y = int(input("Invalid. Enter Y coordinate to add (1 to "+str(screen[0])+"): ")) - 1

    feild[y][x] = typed
  clear()

# [-1, 1], [0, 1], [1, 1]
# [-1, 0], [0, 0], [1, 0]
# [-1,-1], [0,-1], [1,-1]

# checks neighbors of pixels
def neighbor(pixel,field, typed = "#"):
  coords = []
  coords.append([pixel[0]-1, pixel[1]+1])
  coords.append([pixel[0], pixel[1]+1])
  coords.append([pixel[0]+1, pixel[1]+1])
  coords.append([pixel[0]-1, pixel[1]])
  coords.append([pixel[0]+1, pixel[1]])
  coords.append([pixel[0]-1, pixel[1]-1])
  coords.append([pixel[0], pixel[1]-1])
  coords.append([pixel[0]+1, pixel[1]-1])
  
  for i in range(8):
    if coords[i][0] < 0:
      coords[i][0] = len(field[0])-1
    elif coords[i][0] > len(field[0])-1:
      coords[i][0] = 0

    if coords[i][1] < 0:
      coords[i][1] = len(field)-1
    elif coords[i][1] > len(field)-1:
      coords[i][1] = 0
  values = []
  for i2 in range(8):
    temp = field[coords[i2][1]][coords[i2][0]]
    values.append(temp==typed)
  
  count = 0
  for i in range(len(values)):
    if values[i] == True:
      count += 1

  return count

# decides whether pixel should be alive
def decide(count, pixel, typed = "#", typeE = " "):
  if pixel == typed:
    if count == 2 or count == 3:
      return typed
    else:
      return typeE
  else:
    if count == 3:
      return typed
    else:
      return typeE

# updates the feild
def update(feild):
  feild2 = generateField()
  for row in range(len(feild)):
    for column in range(len(feild[0])):
      feild2[row][column] = decide(neighbor([column,row], feild),feild[row][column])
  return feild2

# random selection
def randomize(number, feild, typed = "#"):
  screen = size()
  #print(screen)
  for i in range(number):
    rng = [randint(0,screen[1]-1), randint(0,screen[0]-1)]
    #print(rng)
    feild[rng[1]][rng[0]] = typed

def bounds(origin, feild):
  #print(origin)
  if origin[0] > len(feild[0])-1:
    origin[0]-=len(feild[0])
  elif origin[0] < 0:
    origin[0] += len(feild[0])
  
  if origin[1] > len(feild)-1:
    origin[1] -= len(feild)
  elif origin[1] < 0:
    origin[1] += len(feild)
  #print(origin)
  #a = input("")

def nuke(feild):
  #dims = size()
  # Start position
  start = [randint(0,len(feild[0])-1),randint(0,len(feild)-1)]
  if len(feild[0])>len(feild):
    diameter = [randint(3,int((len(feild[0])-1)/2))]
    diameter.append(int(diameter[0]/2))
  else:
    diameter = [randint(3,int((len(feild[0])-1)/2))]
    diameter.append(int(diameter[0]/2))
  
  if diameter[0] % 2 == 0:
    diameter[0]-=1

  if diameter[1] % 2 == 0:
    diameter[1]-=1

  origin = [int(start[0]-(diameter[0]-1)/2), int(start[1]+(diameter[1]-1)/2)]
  
  bounds(origin, feild)

  nukeType = randint(1,2)
  
  if nukeType == 1:
    for i in range (diameter[0]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[0] += 1
      bounds(origin, feild)
    for i in range(diameter[1]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[1] += 1
      bounds(origin, feild)
    for i in range (diameter[0]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[0] -= 1
      bounds(origin, feild)
    for i in range (diameter[1]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[1] -= 1
      bounds(origin, feild)
    #print("\n")
    #showField(feild)
    #a=input("")

    for row in range (len(feild)):
      for col in range(len(feild[0])):
        if feild[row][col] == "@":
          feild[row][col] = "#"
    #showField(feild)
    #a=input("")
  else:

    for it in range (diameter[1]-1):
      for i in range(diameter[0]-1):
        # Marked
        #print(origin)
        feild[int(origin[1])][int(origin[0])] = "@"
        origin[0] += 1
        bounds(origin, feild)
      origin = [start[0]-(diameter[0]-1)/2, origin[1]+1]
      bounds(origin, feild)

    for row in range (len(feild)):
      for col in range(len(feild[0])):
        if feild[row][col] == "@":
          feild[row][col] = "#"

def rainFire(feild):
  number = 25
  for i in range(number):
    start = [randint(0,len(feild[0])-1),randint(0,len(feild)-1)]

    diameter = [3,3]
  
    origin = [int(start[0]-(diameter[0]-1)/2), int(start[1]+(diameter[1]-1)/2)]
  
    bounds(origin, feild)

    for i in range (diameter[0]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[0] += 1
      bounds(origin, feild)
    for i in range(diameter[1]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[1] += 1
      bounds(origin, feild)
    for i in range (diameter[0]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[0] -= 1
      bounds(origin, feild)
    for i in range (diameter[1]-1):
      feild[int(origin[1])][int(origin[0])] = "@"
      origin[1] -= 1
      bounds(origin, feild)
    
    #print("\n")
    #showField(feild)
    #a=input("")

  for row in range (len(feild)):
    for col in range(len(feild[0])):
      if feild[row][col] == "@":
        feild[row][col] = "#"
    
  #print("\n")
  #showField(feild)
  #a=input("")
    

def simulate(gameScreen, delay = 0.07):
  counts = 1
  bombdrop = 50
  nuketyme = 150
  while True:
    sleep(delay)
    #a = input("")
    clear()
    gameScreen = update(gameScreen)
    showField(gameScreen)
    counts+=1
    """
    if counts % bombdrop == 0:
      rainFire(gameScreen)
    """
    if counts % nuketyme == 0:
      nuke(gameScreen)
    counts+=1
  
    


# add nuking function that randomly adds live cells or kills them. Starting point and dimensions are random. Square blastspace. 

# Program
clear()
#print(size())
gameScreen = generateField()
#add(gameScreen)
randomize(727, gameScreen)
showField(gameScreen)
simulate(gameScreen)
