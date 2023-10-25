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

# music works with .wav or .ogg files that are uncompressed

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

music_frame = Rect((100, 120), (600, 400))

scroll_up = Actor("scrollarrowup", (700, 110))
scroll_down = Actor("scrollarrowdown", (700, 530))

playlist_symbol_1 = Actor("playlist_symbol", (105, 180))
playlist_symbol_2 = Actor("playlist_symbol", (305, 180))
playlist_symbol_3 = Actor("playlist_symbol", (505, 180))
playlist_symbol_4 = Actor("playlist_symbol", (705, 180))
playlist_symbol_5 = Actor("playlist_symbol", (105, 380))
playlist_symbol_6 = Actor("playlist_symbol", (305, 380))
playlist_symbol_7 = Actor("playlist_symbol", (505, 380))
playlist_symbol_8 = Actor("playlist_symbol", (705, 380))


#music template
# music_rect_template = Rect((100, 120+40x), (600, 40))
# music_text_template = screen.draw.text("song name", (130, 130+40x), fontsize=30, color="black")
music_rect = Rect((100, 120), (600, 40))
another_music_rect = Rect((100, 160), (600, 40))

play_name_1 = "playlist one"
play_name_2 = "playlist two"
play_name_3 = "playlist three"
play_name_4 = "playlist four"
play_name_5 = "playlist five"
play_name_6 = "playlist six"
play_name_7 = "playlist seven"
play_name_8 = "playlist eight"

# This is for fullscreen
once = False
once_treeroom = False

scroll = 0

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
            draw_lists()
                                # halloween_music()
        case "rosh":
            screen.fill((237, 223, 24))
            screen.draw.text("Rosh Hashanah Music!", (210, 50), fontsize=50, color="black")
            back_arrow.draw()
            draw_lists()
                                #rosh_music()
        case "dia":
            screen.fill((163, 82, 255))
            screen.draw.text("Dia De Los Muertos Music!", (170, 50), fontsize=50, color="pink")
            back_arrow.draw()
            draw_lists()
                                #dia_music()
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


def draw_lists():    
    playlist_symbol_1.draw()
    playlist_symbol_2.draw()
    playlist_symbol_3.draw()
    playlist_symbol_4.draw()
    playlist_symbol_5.draw()
    playlist_symbol_6.draw()
    playlist_symbol_7.draw()
    playlist_symbol_8.draw()
    
    screen.draw.text(play_name_1, midtop=(105, 260), fontsize=30, color="black")
    screen.draw.text(play_name_2, midtop=(305, 260), fontsize=30, color="black")
    screen.draw.text(play_name_3, midtop=(505, 260), fontsize=30, color="black")
    screen.draw.text(play_name_4, midtop=(705, 260), fontsize=30, color="black")
    screen.draw.text(play_name_5, midtop=(105, 460), fontsize=30, color="black")
    screen.draw.text(play_name_6, midtop=(305, 460), fontsize=30, color="black")
    screen.draw.text(play_name_7, midtop=(505, 460), fontsize=30, color="black")
    screen.draw.text(play_name_8, midtop=(705, 460), fontsize=30, color="black")

# FIXME put in playlists

def name_lists():
    global play_name_1
    global play_name_2
    global play_name_3
    global play_name_4
    global play_name_5
    global play_name_6
    global play_name_7
    global play_name_8
    
    if current_scene == "halloween":
        play_name_1 = "halloween_1"
        play_name_2 = "halloween_2"
        play_name_3 = "halloween_3"
        play_name_4 = "halloween_4"
        play_name_5 = "halloween_5"
        play_name_6 = "halloween_6"
        play_name_7 = "halloween_7"
        play_name_8 = "halloween_8"
    
    if current_scene == "dia":
        play_name_1 = "dia_1"
        play_name_2 = "dia_2"
        play_name_3 = "dia_3"
        play_name_4 = "dia_4"
        play_name_5 = "dia_5"
        play_name_6 = "dia_6"
        play_name_7 = "dia_7"
        play_name_8 = "dia_8"

    if current_scene == "rosh":
        play_name_1 = "rosh_1"
        play_name_2 = "rosh_2"
        play_name_3 = "rosh_3"
        play_name_4 = "rosh_4"
        play_name_5 = "rosh_5"
        play_name_6 = "rosh_6"
        play_name_7 = "rosh_7"
        play_name_8 = "rosh_8"


def open_list(list_name):
    global max_scroll
    global scroll
    global current_scene

#FIXME finish playlist open function based on halloween_music


def halloween_music():
    global max_scroll
    global scroll
    max_scroll = 3
    scroll_down.draw()
    scroll_up.draw()
    if scroll == 0:
        song_name_1 = "sn1"
        song_name_2 = "sn2"
        song_name_3 = "sn3"
        song_name_4 = "sn4"
        song_name_5 = "sn5"
        song_name_6 = "sn6"
        song_name_7 = "sn7"
        song_name_8 = "sn8"
        song_name_9 = "sn9"
        song_name_10 = "sn10"

    if scroll == 1:
        song_name_1 = "sn11"
        song_name_2 = "sn12"
        song_name_3 = "sn13"
        song_name_4 = "sn14"
        song_name_5 = "sn15"
        song_name_6 = "sn16"
        song_name_7 = "sn17"
        song_name_8 = "sn18"
        song_name_9 = "sn19"
        song_name_10 = "sn20"
    
    if scroll ==  2:
        song_name_1 = "sn21"
        song_name_2 = "sn22"
        song_name_3 = "sn23"
        song_name_4 = "sn24"
        song_name_5 = "sn25"
        song_name_6 = "sn26"
        song_name_7 = "sn27"
        song_name_8 = "sn28"
        song_name_9 = "sn29"
        song_name_10 = "sn30"
   
    if scroll ==  3:
        song_name_1 = "sn31"
        song_name_2 = "sn32"
        song_name_3 = "sn33"
        song_name_4 = "sn34"
        song_name_5 = "sn35"
        song_name_6 = "sn36"
        song_name_7 = "sn37"
        song_name_8 = "sn38"
        song_name_9 = "sn39"
        song_name_10 = "sn40"

    screen.draw.rect(music_frame, "brown")
    halloween_frame_1 = Rect((100, 120), (600, 40))
    halloween_frame_2 = Rect((100, 160), (600, 40))
    halloween_frame_3 = Rect((100, 200), (600, 40))
    halloween_frame_4 = Rect((100, 240), (600, 40))
    halloween_frame_5 = Rect((100, 280), (600, 40))
    halloween_frame_6 = Rect((100, 320), (600, 40))
    halloween_frame_7 = Rect((100, 360), (600, 40))
    halloween_frame_8 = Rect((100, 400), (600, 40))
    halloween_frame_9 = Rect((100, 440), (600, 40))
    halloween_frame_10 = Rect((100, 480), (600, 40))
    
    screen.draw.text(song_name_1, (130, 130), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_1, "brown")

    screen.draw.text(song_name_2, (130, 170), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_2, "brown")

    screen.draw.text(song_name_3, (130, 210), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_3, "brown")

    screen.draw.text(song_name_4, (130, 250), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_4, "brown")

    screen.draw.text(song_name_5, (130, 290), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_5, "brown")

    screen.draw.text(song_name_6, (130, 330), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_6, "brown")

    screen.draw.text(song_name_7, (130, 370), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_7, "brown")

    screen.draw.text(song_name_8, (130, 410), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_8, "brown")

    screen.draw.text(song_name_9, (130, 450), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_9, "brown")

    screen.draw.text(song_name_10, (130, 490), fontsize=30, color="black")
    screen.draw.rect(halloween_frame_10, "brown")


def rosh_music():
    global scroll
    global max_scroll
    max_scroll = 1
    scroll_down.draw()
    scroll_up.draw()
    if scroll == 0:
        song_name_1 = "rsn1"
        song_name_2 = "rsn2"
        song_name_3 = "rsn3"
        song_name_4 = "rsn4"
        song_name_5 = "rsn5"
        song_name_6 = "rsn6"
        song_name_7 = "rsn7"
        song_name_8 = "rsn8"
        song_name_9 = "rsn9"
        song_name_10 = "rsn10"

    if scroll == 1:
        song_name_1 = "rsn11"
        song_name_2 = "rsn12"
        song_name_3 = "rsn13"
        song_name_4 = "rsn14"
        song_name_5 = "rsn15"
        song_name_6 = "rsn16"
        song_name_7 = "rsn17"
        song_name_8 = "rsn18"
        song_name_9 = "rsn19"
        song_name_10 = "rsn20"



    screen.draw.rect(music_frame, "brown")
    rosh_frame_1 = Rect((100, 120), (600, 40))
    rosh_frame_2 = Rect((100, 160), (600, 40))
    rosh_frame_3 = Rect((100, 200), (600, 40))
    rosh_frame_4 = Rect((100, 240), (600, 40))
    rosh_frame_5 = Rect((100, 280), (600, 40))
    rosh_frame_6 = Rect((100, 320), (600, 40))
    rosh_frame_7 = Rect((100, 360), (600, 40))
    rosh_frame_8 = Rect((100, 400), (600, 40))
    rosh_frame_9 = Rect((100, 440), (600, 40))
    rosh_frame_10 = Rect((100, 480), (600, 40))
    
    screen.draw.text(song_name_1, (130, 130), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_1, "brown")

    screen.draw.text(song_name_2, (130, 170), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_2, "brown")

    screen.draw.text(song_name_3, (130, 210), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_3, "brown")

    screen.draw.text(song_name_4, (130, 250), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_4, "brown")

    screen.draw.text(song_name_5, (130, 290), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_5, "brown")

    screen.draw.text(song_name_6, (130, 330), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_6, "brown")

    screen.draw.text(song_name_7, (130, 370), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_7, "brown")

    screen.draw.text(song_name_8, (130, 410), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_8, "brown")

    screen.draw.text(song_name_9, (130, 450), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_9, "brown")

    screen.draw.text(song_name_10, (130, 490), fontsize=30, color="black")
    screen.draw.rect(rosh_frame_10, "brown")


def dia_music():
    global scroll
    global max_scroll
    max_scroll = 1
    scroll_down.draw()
    scroll_up.draw()
    if scroll == 0:
        song_name_1 = "dsn1"
        song_name_2 = "dsn2"
        song_name_3 = "dsn3"
        song_name_4 = "dsn4"
        song_name_5 = "dsn5"
        song_name_6 = "dsn6"
        song_name_7 = "dsn7"
        song_name_8 = "dsn8"
        song_name_9 = "dsn9"
        song_name_10 = "dsn10"

    if scroll == 1:
        song_name_1 = "dsn11"
        song_name_2 = "dsn12"
        song_name_3 = "dsn13"
        song_name_4 = "dsn14"
        song_name_5 = "dsn15"
        song_name_6 = "dsn16"
        song_name_7 = "dsn17"
        song_name_8 = "dsn18"
        song_name_9 = "dsn19"
        song_name_10 = "dsn20"



    screen.draw.rect(music_frame, "yellow")
    dia_frame_1 = Rect((100, 120), (600, 40))
    dia_frame_2 = Rect((100, 160), (600, 40))
    dia_frame_3 = Rect((100, 200), (600, 40))
    dia_frame_4 = Rect((100, 240), (600, 40))
    dia_frame_5 = Rect((100, 280), (600, 40))
    dia_frame_6 = Rect((100, 320), (600, 40))
    dia_frame_7 = Rect((100, 360), (600, 40))
    dia_frame_8 = Rect((100, 400), (600, 40))
    dia_frame_9 = Rect((100, 440), (600, 40))
    dia_frame_10 = Rect((100, 480), (600, 40))
    
    screen.draw.text(song_name_1, (130, 130), fontsize=30, color="black")
    screen.draw.rect(dia_frame_1, "yellow")

    screen.draw.text(song_name_2, (130, 170), fontsize=30, color="black")
    screen.draw.rect(dia_frame_2, "yellow")

    screen.draw.text(song_name_3, (130, 210), fontsize=30, color="black")
    screen.draw.rect(dia_frame_3, "yellow")

    screen.draw.text(song_name_4, (130, 250), fontsize=30, color="black")
    screen.draw.rect(dia_frame_4, "yellow")

    screen.draw.text(song_name_5, (130, 290), fontsize=30, color="black")
    screen.draw.rect(dia_frame_5, "yellow")

    screen.draw.text(song_name_6, (130, 330), fontsize=30, color="black")
    screen.draw.rect(dia_frame_6, "yellow")

    screen.draw.text(song_name_7, (130, 370), fontsize=30, color="black")
    screen.draw.rect(dia_frame_7, "yellow")

    screen.draw.text(song_name_8, (130, 410), fontsize=30, color="black")
    screen.draw.rect(dia_frame_8, "yellow")

    screen.draw.text(song_name_9, (130, 450), fontsize=30, color="black")
    screen.draw.rect(dia_frame_9, "yellow")

    screen.draw.text(song_name_10, (130, 490), fontsize=30, color="black")
    screen.draw.rect(dia_frame_10, "yellow")


#FIXME include scroll arrows and scrolling functionality next        


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
    global max_scroll
    global scroll
    global current_scene
    if halloween_pumpkin.collidepoint(pos):
        if current_scene == "setup":
            start_halloween()
    if roshhashanah_bottle.collidepoint(pos):
        if current_scene == "setup":
            start_rosh()
    if diadelos_skull.collidepoint(pos):
        if current_scene == "setup":
            start_dia()
    if fall_tree_background.collidepoint(pos):
        if current_scene == "setup":
            if not once_treeroom:
                enter_tree_room()
    if back_arrow.collidepoint(pos):
        if current_scene in ["tree_room", "halloween", "rosh", "dia"]:
            current_scene = "setup"
    if scroll_down.collidepoint(pos):
        if current_scene == "halloween" or "rosh" or "dia":
            if scroll < max_scroll:
                scroll = scroll + 1
    if scroll_up.collidepoint(pos):
        if current_scene == "halloween" or "rosh" or "dia":
            if scroll > 0:
                scroll = scroll - 1
    if playlist_symbol_1.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_1)
        if current_scene == "dia":
            open_list(dia_1)
        if current_scene == "rosh":
            open_list(rosh_1)
    if playlist_symbol_2.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_2)
        if current_scene == "dia":
            open_list(dia_2)
        if current_scene == "rosh":
            open_list(rosh_2)
    if playlist_symbol_3.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_3)
        if current_scene == "dia":
            open_list(dia_3)
        if current_scene == "rosh":
            open_list(rosh_3)
    if playlist_symbol_4.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_4)
        if current_scene == "dia":
            open_list(dia_4)
        if current_scene == "rosh":
            open_list(rosh_4)
    if playlist_symbol_5.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_5)
        if current_scene == "dia":
            open_list(dia_5)
        if current_scene == "rosh":
            open_list(rosh_5)
    if playlist_symbol_6.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_6)
        if current_scene == "dia":
            open_list(dia_6)
        if current_scene == "rosh":
            open_list(rosh_6)
    if playlist_symbol_7.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_7)
        if current_scene == "dia":
            open_list(dia_7)
        if current_scene == "rosh":
            open_list(rosh_7)
    if playlist_symbol_8.collidepoint(pos):
        if current_scene == "halloween":
            open_list(halloween_8)
        if current_scene == "dia":
            open_list(dia_8)
        if current_scene == "rosh":
            open_list(rosh_8)
    


# this function is called every frame
def update():
    name_lists()
    pass


# This has to be the last line in the program
pgzrun.go()
