from microbit import *

def set_pix(pos, turnOn = True):
    brightness = 0
    if turnOn:
        brightness = 9
    display.set_pixel(pos[0], pos[1], brightness)

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
    
def main():
    # Init snake
    snake = [(2,3), (2,4)]
    set_pix(snake[0])
    set_pix(snake[1])
    curDir = 0

    while True:
        sleep(1000)
        curDir = getDir(curDir)
        snakeHead = getSnakeHead(snake, curDir)
        snake = moveSnake(snakeHead, snake)

main()