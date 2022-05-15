from microbit import *
from random import choice

def set_pix(pos, turnOn = True, brightness = 9):
    if not turnOn:
        brightness = 0
    display.set_pixel(pos[0], pos[1], brightness)

def growSnake(newPos, curSnake):
    newSnake = [newPos]
    newSnake.extend(curSnake)
    set_pix(newPos, True)
    return newSnake

def moveSnake(newPos, curSnake):
    newSnake = [newPos]
    newSnake.extend(curSnake)
    set_pix(newPos, True)
    set_pix(curSnake[-1], False)
    newSnake.pop()
    return newSnake
    
def getSnakeHead(snake, curDir):
    if curDir == 0:
        snakeHead = (snake[0][0], (snake[0][1]-1)%5)
    elif curDir == 1:
        snakeHead = ((snake[0][0]+1)%5, snake[0][1])
    elif curDir == 2:
        snakeHead = (snake[0][0], (snake[0][1]+1)%5)
    else: # curDir == 3
        snakeHead = ((snake[0][0]-1)%5, snake[0][1])
    return snakeHead
    
def getDir(curDir):
    if button_a.is_pressed() and button_b.is_pressed():
        return curDir
    elif button_a.is_pressed():
        return (curDir-1) % 4
    elif button_b.is_pressed():
        return (curDir+1) % 4
    else:
        return curDir
    
def getApple(snake):
    positions = []
    for i in range(5):
        for j in range(5):
            positions.append((i,j))
    positions = list(filter(lambda x: x not in snake, positions))
    apple = choice(positions)
    set_pix(apple, brightness=2)
    return apple
    
def main():
    # Init snake
    snake = [(2,3), (2,4)]
    set_pix(snake[0])
    set_pix(snake[1])
    curDir = 0
    apple = getApple(snake)

    while True:
        sleep(1000)
        curDir = getDir(curDir)
        snakeHead = getSnakeHead(snake, curDir)
        
        if snakeHead == apple:
            snake = growSnake(snakeHead, snake)
            apple = getApple(snake)
        else:
            snake = moveSnake(snakeHead, snake)

main()