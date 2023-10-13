# event.python/games or smth like that from Al Sweigart

# copyright matters

# how to use pygame zero:
# run the program and go to ports
# open the link that starts with desktop under forwarded address
# password is "vscode"
# enjoy

# set a variable as a corrosponding image by typing alien = Actor('alien')
# to set a position for the variable, use alien.pos = 30, 40
# to render in the image, use alien.draw()
# to preset a position for a varibale, use alien.position1 = 12, 36
# update() is called every frame
# you can move images around with alien.left += 2
# to interact with mouse clicks, use function on_mouse_down(pos)
#   if alien.collidepoint(pos):
#       do whatever
# position variable above is not required, pygame zero works anyway
# there is a button parameter for on_mouse_down(), so you should use
#   if button == mouse.LEFT and alien.collidepoint(pos):
#       do whatever
# to play sound, use sounds.songname.play()
# remember you can call functions inside of other functions (not related to above lol)
# in order to do something time based, use clock.schedule_unique(set_alien_happy, 1.0)
# This will cause the function set_alien_happy() to be called after 1 second
# schedule_unique prevents the same function from happening twice simultaneously
# use center.actorname = (x,y) to put actors where i want them

# Keep this at the top
import pgzrun
import pygame

WIDTH = 800
HEIGHT = 600

# Important colors
brown = (128, 66, 8)

# Important actors and positions

pick_the_holiday_vibe = Actor('pick the holiday vibe')
pick_the_holiday_vibe.pos = 400, 50

halloween_pumpkin = Actor('pumkinsquarepng', (200, 200))
square_hal_pumpkin = Rect((140, 140), (120, 120))

roshhashanah_bottle = Actor('winesquare', (600,200))
square_rosh_bottle = Rect((540, 140), (120, 120))

diadelos_skull = Actor('newdiadelossquare', (200, 450))
square_dia_skull = Rect((140,390), (120, 120))

# This is for fullscreen
once = False

#This is a setup function I think maybe it might be the main loop also
def draw():
    global once
    if not once:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        once = True
    screen.fill((252, 174, 28))
    screen.draw.text('Which holiday are you interested in?', (100, 50), fontsize = 50, color = 'brown')
    halloween_pumpkin.draw()
    screen.draw.rect(square_hal_pumpkin, 'brown')
    roshhashanah_bottle.draw()
    screen.draw.rect(square_rosh_bottle, 'brown')
    diadelos_skull.draw()
    screen.draw.rect(square_dia_skull, 'brown')
    


def update():
    pass


# This has to be the last line in the program
pgzrun.go()
