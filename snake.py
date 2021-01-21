import random
import pygame


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
snake = [500, 300, 10, 10]
displayHeight = 600
displayWidth = 1000
snakeSpeed = 15
snakeSize = 10

pygame.init()

display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Derrick\'s Snake Game')

gameOver = False

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)
scoreFont = pygame.font.SysFont("comicsansms", 35)


def score(score):
    value = scoreFont.render("Your Score: " + str(score), True, red)
    display.blit(value, [0, 0])


def drawSnake(snakeBlock, snakeList):
	for x in snakeList:
		pygame.draw.rect(display, white, [x[0], x[1], snakeBlock, snakeBlock])


def message(msg, color):
	message = font_style.render(msg, True, color)
	display.blit(message, [displayWidth / 6, displayHeight / 3])


def gameLoop():
	gameOver = False
	gameClose = False

	x1 = displayWidth / 2
	y1 = displayHeight / 2

	x1_change = 0
	y1_change = 0

	snakeList = []
	snakeLength = 1

	foodX = round(random.randrange(0, displayWidth - snakeSize) / 10.0) * 10.0
	foodY = round(random.randrange(0, displayHeight - snakeSize) / 10.0) * 10.0

	while not gameOver:
		while gameClose:
			display.fill(white)
			message("You Lost! Press Q-Quit or C-Play Again", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = True
						gameClose = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -snakeSize
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snakeSize
					y1_change = 0
				elif event.key == pygame.K_UP:
					y1_change = -snakeSize
					x1_change = 0
				elif event.key == pygame.K_DOWN:
					y1_change = snakeSize
					x1_change = 0

		if x1 >= displayWidth or x1 < 0 or y1 >= displayHeight or y1 < 0:
			gameClose = True

		x1 += x1_change
		y1 += y1_change

		display.fill(black)
		pygame.draw.rect(display, white, [x1, y1, snakeSize, snakeSize])
		pygame.draw.rect(display, red, [foodX, foodY, snakeSize, snakeSize])

		snakeBlock = [x1, y1]
		snakeList.append(snakeBlock)

		if len(snakeList) > snakeLength:
			del snakeList[0]

		for x in snakeList[:-1]:
			if x == snakeBlock:
				gameClose = True

		drawSnake(snakeSize, snakeList)
		score(snakeLength - 1)

		pygame.display.update()

		if x1 == foodX and y1 == foodY:
			foodX = round(random.randrange(0, displayWidth - snakeSize) / 10.0) * 10.0
			foodY = round(random.randrange(0, displayHeight - snakeSize) / 10.0) * 10.0
			snakeLength += 1

		clock.tick(snakeSpeed)

	pygame.quit()
	quit()


gameLoop()
