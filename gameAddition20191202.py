# Based on code at:
# http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# 1 - Import pygame library ####################################################
import pygame
from pygame.locals import *

# 2 - Set game global variables ################################################
boardsize = (512, 512)
screen = pygame.display.set_mode(boardsize)
width, height, margin = 100, 100, 2
BLACK = (0, 0, 0)
WHITE = (255,255,255)
grid = [] # 2D array (list of lists) for board
player = pygame.image.load('img\player.jpg').convert()
playerCoord = [0,0]
icon0 = pygame.image.load('img\icon0.jpg').convert() 
icon1 = pygame.image.load('img\icon1.jpg').convert()
icon2 = pygame.image.load('img\icon2.jpg').convert()
icon3 = pygame.image.load('img\icon3.jpg').convert()

# 3 - Define game functions ####################################################
## 3a - Initialize the game board
def initBoard(): 
  for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0) # all values set to 0
  # Set hard-coded start locations for player and icons:        
  grid[0][0] = 1  # player icon; value of 1 is player location
  grid[0][2] = 10 # icon 0 location set by a value of 10
  grid[3][1] = 11 # icon 1 location set by a value of 11
  grid[2][2] = 12 # icon 2 location set by a value of 12
  grid[4][3] = 13 # icon 3 location set by a value of 13

## 3b - Draw player/icon on the board
def drawIcon(rw,cl,iconName):
  screen.blit(iconName,((margin+width)*cl + margin,(margin+height)*rw + margin))
  
## 3c - Update the grid for the board
def updateBoard():
  for row in range(5):
    for column in range(5):
      color = WHITE             
      pygame.draw.rect(screen,color,[(margin + width) * column + margin,
                                     (margin + height) * row + margin,
                                      width, height])
      if grid[row][column] == 10:  #icon0 location
        drawIcon(row,column,icon0)  
      if grid[row][column] == 11:  #icon1 location
        drawIcon(row,column,icon1)  
      if grid[row][column] == 12:  #icon2 location
        drawIcon(row,column,icon2)  
      if grid[row][column] == 13:  #icon3 location
        drawIcon(row,column,icon3)    
      if grid[row][column] == 1:  #player location
        drawIcon(row,column,player)  

## 3d - Adjust score and print out a message if increased
def adjustScore(scoreP):
  success = 0
  if grid[playerCoord[0]][playerCoord[1]] == 10:
    print("Is this statement true or false? :: A variable is a location where a computer can store information")
    response = input("Enter (F)alse or (T)rue: ")
    if (response == "T" or response == "t"):
      success = 1
  elif grid[playerCoord[0]][playerCoord[1]] == 11:
    print("Is this statement true or false? :: A loop is when the computer doesn't repeat instructions.")
    response = input("Enter (F)alse or (T)rue: ")
    if (response == "F" or response == "f"):
      success = 1
  elif grid[playerCoord[0]][playerCoord[1]] == 12:
    print("Is this statement true or false? :: A conditional is when the computer uses data to make decisions for you.")
    response = input("Enter (F)alse or (T)rue: ")
    if (response == "T" or response == "t"):
      success = 1
  elif grid[playerCoord[0]][playerCoord[1]] == 13:
    print("Is this statement true or false? :: A function is a group of bundled commands that you can call when you need them.")
    response = input("Enter (F)alse or (T)rue: ")
    if (response == "T" or response == "t"):
      success = 1    
  if success == 1:
    scoreP += 1
    print("You have learned "+str(scoreP)+" of the Core 4")
  elif success == 0 and grid[playerCoord[0]][playerCoord[1]] >= 10:
    print("You answered incorrectly. Study https://github.com/jinnyyan/gwc19-game/blob/master/Core4ReferenceSheet.pdf")
  return scoreP, success

## 3e - Handle player movement
def movePlayer(scoreParam):
  # Based on how-to at:
  # https://opensource.com/article/17/12/game-python-moving-player
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True; pygame.quit()
        sys.exit(); numlitter == 0
      # only handle key releases for simplicity (KEYUP not KEYDOWN)
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == ord('a'):
          if playerCoord[1] > 0:            
            grid[playerCoord[0]][playerCoord[1]] = 0 #move off of old square
            playerCoord[1] -= 1
            scoreParam, outcome = adjustScore(scoreParam)
            if grid[playerCoord[0]][playerCoord[1]] >= 10:
              if outcome == 1:
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player
              else:
                playerCoord[1] += 1                      #set coord back
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player back
            else:
              grid[playerCoord[0]][playerCoord[1]] = 1 #move to new empty square
        elif event.key == pygame.K_RIGHT or event.key == ord('d'):
          if playerCoord[1] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0 #move off of old square
            playerCoord[1] += 1
            scoreParam, outcome = adjustScore(scoreParam)
            if grid[playerCoord[0]][playerCoord[1]] >= 10:
              if outcome == 1:
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player
              else:
                playerCoord[1] -= 1                      #set coord back
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player back
            else:
              grid[playerCoord[0]][playerCoord[1]] = 1 #move to new empty square                
        elif event.key == pygame.K_UP or event.key == ord('w'):
          if playerCoord[0] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0 #move off of old square
            playerCoord[0] -= 1
            scoreParam, outcome = adjustScore(scoreParam)
            if grid[playerCoord[0]][playerCoord[1]] >= 10:
              if outcome == 1:
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player
              else:
                playerCoord[0] += 1                      #set coord back
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player back
            else:
              grid[playerCoord[0]][playerCoord[1]] = 1 #move to new empty square                
        elif event.key == pygame.K_DOWN or event.key == ord('s'):
          if playerCoord[0] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0 #move off of old square
            playerCoord[0] += 1
            scoreParam, outcome = adjustScore(scoreParam)
            if grid[playerCoord[0]][playerCoord[1]] >= 10:
              if outcome == 1:
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player
              else:
                playerCoord[0] -= 1                      #set coord back
                grid[playerCoord[0]][playerCoord[1]] = 1 #move player back
            else:
              grid[playerCoord[0]][playerCoord[1]] = 1 #move to new empty square                
        elif event.key == ord('q'):
          print('quit game'); pygame.quit()
          break          
  return scoreParam

## 3f - Provide initial instructions
def gameInstructions():
  print("Collect all of the Core 4 programming concepts!\n")
  print("To play, make sure you can see both the game board and the shell screen.")
  print("As you move through the board, you will encounter items.")
  print("To collect these items, you will answer questions in the shell about that item.")
  print("***Put your cursor at the end of the bottom line before you type an answer***")
  print("If you answer incorrectly, you will stay in the same location you were.")
  print("Remember, you can always try again, and learn from the incorrect answer.")  
  print("IMPORTANT: Be sure to click on the screen or the shell as appropriate.")
  print("You will have to click between these screens to play.")
  print("Now go show us what you know!\n")

# 4 - Define main game #########################################################
def gameFunct():
  ## 4a - Initialize game
  pygame.init()
  initBoard()
  clock = pygame.time.Clock()
  score = 0
  gameInstructions()
  ## 4b - keep looping until exit condition met
  while (score < 4):
    score = movePlayer(score)  # Handle player movement
    updateBoard() # Update the grid for the board
    clock.tick(60) # In milliseconds (https://www.pygame.org/docs/ref/time.html)
    pygame.display.flip() # Redraw the board
    if score == 4: # Check for exit condition congratulatory message
      print("Congratulations on learning all of the Core 4!")
      print("Now practice practice practice and create cool code!")
  pygame.quit() # Quit the game

# Run automatically upon load/F5 ###############################################
if __name__ == "__main__":
  gameFunct()
