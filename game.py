# # Raneem Tarfa and Natalia Makarova
# rt8fsn and nvm6nf

# #game called duck jump, as player(a cute duck) goes upward on platforms,
# score increases;  if duck falls, it loses a life (out of 3); if loses 3 lives, game is over
#if duck goes off screen, game over

import pygame 
import gamebox
import random


#direction sin title screen (press space to start, up down etc)


camera=gamebox.Camera(800,550)
game_on='start_screen'

duck=gamebox.from_image(400,457,'duck.png')
duck.scale_by(0.05)
ground=gamebox.from_color(400,500,'dark green',800,100)

platform=gamebox.from_color(random.randint(50,750),random.randint(350,360),'yellow',160,10)
platform2=gamebox.from_color(random.randint(50,750),random.randint(250,320),'red',160,10)
platform3=gamebox.from_color(random.randint(50,750),random.randint(150,220),'purple',160,10)
platform4=gamebox.from_color(random.randint(50,750),random.randint(50,120),'blue',160,10)




fox=gamebox.from_image(platform3.x, platform3.top,'fox.png')
fox.scale_by(0.05)

def fox_position():
    '''designates random position for fox'''
    fox_platform=random.randint(1,3)
    if fox_platform==2:
        fox.x = platform2.x
        fox.bottom=platform2.top
    if fox_platform==3:
        fox.x = platform3.x
        fox.bottom=platform3.top
    if fox_platform==4:
        fox.x=platform4.x
        fox.bottom=platform4.top

fox_position()



obstacles=[ground,platform, platform2, platform3,platform4]
platforms=[platform,platform2,platform3,platform4]
life_boxes=[gamebox.from_image(600,camera.top+50,'heart.png'),
            gamebox.from_image(650,camera.top+50,'heart.png'),
            gamebox.from_image(700,camera.top+50,'heart.png')]


text1=gamebox.from_text(400,200,"Duck Duck Jump",80,'white')
text2=gamebox.from_text(400,290,"Natalia Makarova (nvm6mf) & Raneem Tarfa (rt8fsn)",40,'white')
text3=gamebox.from_text(400,340,"Press space to start. Press up/right/left arrows to move.",35,'white')


title_screen=[text1,text2,text3]

gravity=0.9
lives=3
score=0
level=1

level_text=gamebox.from_text(60,camera.top+50,"LEVEL"+str(level),40,'white')

extra_life=gamebox.from_image(600,camera.top+50,'heart2.png')
extra_life.scale_by(0.1)
extra_life_collected=False

def draw_lives(num_lives):
    '''draws the lives'''
    first_x=camera.right-20
    y=camera.top+50
    for i in range(num_lives):
        life=gamebox.from_image(first_x-i*40,y,'heart.png')
        camera.draw(life)

def count_score():
    '''counts the score with each tick (relates to levels)'''
    global score
    while game_on=='game':
        return 1
    return 0

def overlap():
    '''prevents overlapping among variables'''
    platform.move_to_stop_overlapping(platform2, 75, 150)
    platform2.move_to_stop_overlapping(platform3, 75, 150)
    platform3.move_to_stop_overlapping(platform, 75, 150)
    platform.move_to_stop_overlapping(platform4, 75, 150)
    platform2.move_to_stop_overlapping(platform4, 75, 150)
    platform3.move_to_stop_overlapping(platform4, 75, 150)
    for item in platforms:
        item.move_to_stop_overlapping(ground,75,100)
    fox.move_to_stop_overlapping(extra_life,25,30)

def fox_move():
    '''moves fox back and forth across space'''
    direction='right'
    if direction == 'right':
      fox.x += 1
    for thing in platforms:
      if fox.right == thing.right:
          direction = 'left'
    while direction == 'left':
      fox.x -= 1
      for thing in platforms:
          if fox.left == thing.left:
              direction = 'right'
              break


bckgd= ''
def level_color():
    '''chnages background color and speed of levels'''
    global lives
    global extra_life_collected
    global level_text
    global bckgd
    global fox
    if level==1:
        bckgd='light blue'
        # if bckgd=='light blue':
        # camera.draw(level_text)
        # level_text.y -= 2
    if level==2:

        backgd='orange'
        camera.clear('orange')
        camera.y-=1
        if extra_life.bottom>platform2.y:
            extra_life.y-=150
        # extra_life_collected = 'one'
        # if duck.touches(extra_life) and not extra_life_collected:
        #     lives += 1
        #     extra_life_collected = True
        # draw_lives(lives)
        # camera.draw(extra_life)
        # draw_lives(lives)


        level_text = gamebox.from_text(60, camera.top + 50, "LEVEL" + str(level), 40, 'white')

    if level==3:
        bckgd='green'
        camera.clear('green')
        camera.y-=1
        # camera.draw(extra_life)
        # if duck.touches(extra_life) and not extra_life_collected:
        #     lives += 1
        #     extra_life_collected = True
        # draw_lives(lives)

        level_text = gamebox.from_text(60, camera.top + 50, "LEVEL" + str(level), 40, 'white')

    if level==4:
        bckgd='pink'
        camera.clear('pink')
        camera.y-=1
        # camera.draw(extra_life)
        # if duck.touches(extra_life) and not extra_life_collected:
        #     lives += 1
        #     extra_life_collected = True
        # draw_lives(lives)

        level_text = gamebox.from_text(60, camera.top + 50, "LEVEL" + str(level), 40, 'white')


    level_text.y = camera.top + 50
    camera.draw(level_text)
    # fox = gamebox.from_image(platform3.x, platform3.top, 'fox.png')
    # fox.scale_by(0.05)
    # fox_position()
    # camera.draw(fox)
    # fox_move()
    overlap()

things=[duck,ground,platform, platform2, platform3, platform4,fox]

def duck_offscreen(duck):
    #returns duck to ground
    return duck.top>camera.bottom

def start(keys):
    #displays title screen
    global game_on
    camera.clear('light blue')
    for item in title_screen:
        camera.draw(item)
    if pygame.K_SPACE in keys:
        # print("round 2")
        game_on='game'


def game_over(keys):
    #displays end screen when game is over
    global game_on
    camera.clear('black')
    game_over = gamebox.from_text(400, 300, "GAME OVER", 150, "white")
    camera.draw(game_over)
    camera.y = 300
    camera.x = 400
    if pygame.K_SPACE in keys:
        game_on = 'start_screen'
        keys.clear()
        return True



def game(keys):
    '''actual gameplay after hitting space'''
    global game_on
    global lives
    global score
    global level
    global extra_life_collected
    global  level_text
    camera.clear('light blue')
    # print("starting game 2")
    overlap()
    # fox_move()
    for item in obstacles:
        duck.move_to_stop_overlapping(item)
    level_color()
    draw_lives(lives)
    for item in things:
        camera.draw(item)  # if game over fix
    if pygame.K_UP in keys:
        for item in obstacles:
            if duck.bottom == item.top:
                duck.y -= 175
    if pygame.K_RIGHT in keys:
        duck.x += 25
    if pygame.K_LEFT in keys:
        duck.x -= 25
    duck.y += duck.speedy
    duck.speedy += gravity
    camera.y -= 2
    score += count_score()


    # for thing in platforms:
    #     if duck.bottom_touches(thing):
    #         score+=1

    if duck_offscreen(duck) or duck.touches(fox):
        lives -= 1
        score = 0
        level = 1
        level_text = gamebox.from_text(60, camera.top + 50, "LEVEL" + str(level), 40, 'white')
        # camera.draw(level_text)
        duck.bottom = ground.top
        camera.bottom = ground.bottom
        platform.center = (random.randint(50, 750), random.randint(350, 360))
        platform2.center = (random.randint(50, 750), random.randint(250, 320))
        platform3.center = (random.randint(50, 750), random.randint(150, 220))
        platform4.center = (random.randint(50, 750), random.randint(50, 120))
        # fox_position()
        fox.x = platform4.x
        fox.bottom = platform4.y
        if fox.top > camera.bottom:
            fox.x = platform4.x
            fox.bottom = platform4.top
        draw_lives(lives)
        level_color()
        score += count_score()

    fox_move()
    # fox_position()

    if score % 200 == 0:
        level += 1
        # camera.draw(level_text)

    if lives == 0:
        game_on = 'end'

    for item in platforms:
        if item.top > camera.bottom:  # some issues here
            item.x = random.randint(200, 750)
            item.y -= 200
            overlap()

    if duck.touches(extra_life) and not extra_life_collected:
        lives += 1
        extra_life_collected = True
    draw_lives(lives)
    if not extra_life_collected:  # and game_on==True:
        camera.draw(extra_life)


def tick(keys):
    '''allows player to press keys and displays the game'''
    global game_on
    if game_on=='start_screen':
        start(keys)
    if game_on=='game':
        game(keys)
    if game_on =='end':
        game_over(keys)
        # if pygame.K_SPACE in keys:
        #     print("im here")
        #     game_on = 'start_screen'
        #     keys.clear()
            # if pygame.K_SPACE in keys:
            #     game_on='game'


    #
    # print(score)





    camera.display()




gamebox.timer_loop(30,tick)



#
# lives/health bar
#
# camera scrolls up as player scrolls up
#
# moving enemies on some platforms, if duck touches them then loses a life
#
# can collect lives randomly spotted on platforms
#
# background changes with every level(color;blue, sunset, nighttime)
#
# more enemies at every level (camera maybe also scrolls up faster if not at same rate as player)
#
# first background os sky with clouds
#
# duck can jump up with buttom and move left/right
#
# platforms are spaced equidistantly upward
#
# duck cannot jump in middair (maybe change this)
#
# enemies= snakes
#
#
#
#
