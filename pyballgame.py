from pygame import *

ball_image = image.load('ball.png')

finished_playing = False

ball_pos_x = 0
ball_pos_y = 0
ball_move_x = 1
ball_move_y = 1

init()
screen = display.set_mode((640, 480))
display.set_caption('Ball zinga !')

while finished_playing == False:
    screen.fill(1)
    screen.blit(ball_image, (ball_pos_x, ball_pos_y))
    display.update()

    time.delay(1)

    ball_pos_x += ball_move_x
    ball_pos_y += ball_move_y

    if ball_pos_x > 600:
        ball_move_x = -1
    if ball_pos_x < 0:
        ball_move_x = 1
    if ball_pos_y > 400:
        ball_move_y = -1
    if ball_pos_y < 0:
        ball_move_y = 1

for e in event.get():
    if e.type == KEYUP:
        if e.type == K_ESCAPE:
            finished_playing = True

