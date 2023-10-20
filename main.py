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
pink = (206, 30, 212)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (237, 223, 24)

# Important actors and positions
pick_the_holiday_vibe = Actor("pick the holiday vibe")
pick_the_holiday_vibe.pos = 400, 50

halloween_pumpkin = Actor("pumkinsquarepng", (200, 200))
square_hal_pumpkin = Rect((140, 140), (120, 120))

roshhashanah_bottle = Actor("winesquare", (600, 200))
square_rosh_bottle = Rect((540, 140), (120, 120))

diadelos_skull = Actor("newdiadelossquare", (400, 200))
square_dia_skull = Rect((340, 140), (120, 120))

fall_tree_background = Actor("falltrees", (400, 455))

dancing_tree = Actor("dancingtreeres", (400, 375))
dancing_tree_opposite = Actor("dancingtreeresotherway", (400, 375))

back_arrow = Actor("back_arrow", (50, 560))

# This is for fullscreen
once = False
once_treeroom = False

treeside = 0

current_scene = "setup"


# This is the main loop and is called every frame. The current_scene variable dictates
# what is shown on the screen based on the case.
def draw():
    global once
    global once_treeroom
    global treeside
    if not once:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        once = True
    screen.clear()
    match current_scene:
        case "setup":
            screen.fill((252, 174, 28))
            screen.draw.text("Which holiday are you interested in?", (100, 50), fontsize=50, color="brown",)
            screen.draw.text("Halloween", (160, 270), fontsize=25, color="brown",)
            halloween_pumpkin.draw()
            screen.draw.rect(square_hal_pumpkin, "brown")
            screen.draw.text("Rosh Hashanah", (540, 270), fontsize=25, color="brown",)
            roshhashanah_bottle.draw()
            screen.draw.rect(square_rosh_bottle, "brown")
            screen.draw.text("Dia De Los Muertos", (320, 270), fontsize=25, color="brown",)
            diadelos_skull.draw()
            screen.draw.rect(square_dia_skull, "brown")
            fall_tree_background.draw()
        case "halloween":
            screen.fill((255, 144, 0))
            screen.draw.text("Halloween Music!", (250, 50), fontsize=50, color="yellow")
            back_arrow.draw()
        case "rosh":
            screen.fill((237, 223, 24))
            screen.draw.text("Rosh Hashanah Music!", (210, 50), fontsize=50, color="black")
            back_arrow.draw()
        case "dia":
            screen.fill((163, 82, 255))
            screen.draw.text("Dia De Los Muertos Music!", (170, 50), fontsize=50, color="pink")
            back_arrow.draw()
        case "tree_room":
            screen.fill((56, 36, 0))
            screen.draw.text(
                "You have entered the Tree Room", (125, 50), fontsize=50, color="brown"
            )
            if not once_treeroom:
                once_treeroom = True
                clock.schedule_interval(fliptree, 0.7)
            if treeside == 0:
                dancing_tree.draw()
            if treeside == 1:
                dancing_tree_opposite.draw()
            back_arrow.draw()


def start_halloween():
    global current_scene
    current_scene = "halloween"


def start_rosh():
    global current_scene
    current_scene = "rosh"


def start_dia():
    global current_scene
    current_scene = "dia"


def enter_tree_room():
    global current_scene
    current_scene = "tree_room"
    # music.play("treeroom")


def fliptree():
    global treeside
    if treeside == 0:
        dancing_tree.draw()
        treeside = 1
    else:
        dancing_tree_opposite.draw()
        treeside = 0


def draw_sample_text():
    screen.draw.text("sample", (150, 50), fontsize=50, color="brown")


# this function deals with whenever the mouse is clicked
def on_mouse_down(pos):
    global current_scene
    if halloween_pumpkin.collidepoint(pos):
        start_halloween()
    if roshhashanah_bottle.collidepoint(pos):
        screen.clear()
        start_rosh()
    if diadelos_skull.collidepoint(pos):
        screen.clear()
        start_dia()
    if fall_tree_background.collidepoint(pos):
        if not once_treeroom:
            enter_tree_room()
    if back_arrow.collidepoint(pos):
        if current_scene == "tree_room" or "halloween" or "rosh" or "dia":
            current_scene = "setup"


# this function is called every frame
def update():
    pass


# This has to be the last line in the program
pgzrun.go()
