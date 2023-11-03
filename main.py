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
# use function music.play_once(name) to play a song once
# use function music.queue(name) to queue a song afterwards
# music.pause() pauses whatever is playing
# music.unpause() unpauses
# music.is_playing() returns True if music is playing - use to prevent bugs

# Keep this at the top
import pgzrun
import pygame

# this is the project's resolution window
WIDTH = 800
HEIGHT = 600

# Important colors
brown = (128, 66, 8)
pink = (206, 30, 212)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (237, 223, 24)

# Important actors, rectangles and positions
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

pause_button = Actor("pause_button", midtop=(400, 520))
play_button = Actor("play_button", midtop=(400, 520))

playlist_symbol_1 = Actor("playlist_symbol", (105, 180))
playlist_symbol_2 = Actor("playlist_symbol", (305, 180))
playlist_symbol_3 = Actor("playlist_symbol", (505, 180))
playlist_symbol_4 = Actor("playlist_symbol", (705, 180))
playlist_symbol_5 = Actor("playlist_symbol", (105, 380))
playlist_symbol_6 = Actor("playlist_symbol", (305, 380))
playlist_symbol_7 = Actor("playlist_symbol", (505, 380))
playlist_symbol_8 = Actor("playlist_symbol", (705, 380))

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


# music template
# music_rect_template = Rect((100, 120+40x), (600, 40))
# music_text_template = screen.draw.text("song name", (130, 130+40x), fontsize=30, color="black")
music_rect = Rect((100, 120), (600, 40))
another_music_rect = Rect((100, 160), (600, 40))

#initial playlist names for debugging proper naming
play_name_1 = "playlist one"
play_name_2 = "playlist two"
play_name_3 = "playlist three"
play_name_4 = "playlist four"
play_name_5 = "playlist five"
play_name_6 = "playlist six"
play_name_7 = "playlist seven"
play_name_8 = "playlist eight"

# This is for fullscreen, a bunch of once variables, and initial values of variables to avoid bugs
once = False
once_treeroom = False
load_pause_once = False
pause_or_play = "pause"
playlist_currently_open = "none"
scroll = 0
playlist_that_is_currently_open = "none"
treeside = 0
global_list_holiday = "none"
global_list_num = 0
waiting_on_escape = False
waiting_on_mouse = False
current_scene = "setup"
is_playlist_currently_open = False


# This is the main loop and is called every frame. The current_scene variable dictates
# what is shown on the screen based on the case.
def draw():
    global once
    global once_treeroom
    global treeside
    global playlist_currently_open
    global is_playlist_currently_open
    global load_pause_once
    global pause_or_play
    if not once:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.init()
        once = True
    screen.clear()
    match current_scene:
        case "setup":
            screen.fill((252, 174, 28))
            screen.draw.text(
                "Which holiday are you interested in?",
                (100, 50),
                fontsize=50,
                color="brown",
            )
            screen.draw.text(
                "Halloween",
                (160, 270),
                fontsize=25,
                color="brown",
            )
            halloween_pumpkin.draw()
            screen.draw.rect(square_hal_pumpkin, "brown")
            screen.draw.text(
                "Rosh Hashanah",
                (540, 270),
                fontsize=25,
                color="brown",
            )
            roshhashanah_bottle.draw()
            screen.draw.rect(square_rosh_bottle, "brown")
            screen.draw.text(
                "Dia De Los Muertos",
                (320, 270),
                fontsize=25,
                color="brown",
            )
            diadelos_skull.draw()
            screen.draw.rect(square_dia_skull, "brown")
            fall_tree_background.draw()
        case "halloween":
            screen.fill((255, 144, 0))
            if not is_playlist_currently_open:
                screen.draw.text(
                    "Halloween Music!", (250, 50), fontsize=50, color="yellow"
                )
                back_arrow.draw()
                draw_lists()
            if is_playlist_currently_open:
                if playlist_currently_open == "halloween":
                    back_arrow.draw()
                    open_list("halloween", global_list_num)
                    draw_songs()

        case "rosh":
            screen.fill((237, 223, 24))
            if not is_playlist_currently_open:
                screen.draw.text(
                    "Rosh Hashanah Music!", (210, 50), fontsize=50, color="black"
                )
                back_arrow.draw()
                draw_lists()
            if is_playlist_currently_open:
                if playlist_currently_open == "rosh":
                    back_arrow.draw()
                    open_list("rosh", global_list_num)
                    draw_songs()
        case "dia":
            screen.fill((163, 82, 255))
            if not is_playlist_currently_open:
                screen.draw.text(
                    "Dia De Los Muertos Music!", (170, 50), fontsize=50, color="pink"
                )
                back_arrow.draw()
                draw_lists()
            if is_playlist_currently_open:
                print("dia list is open")
                if playlist_currently_open == "dia":
                    print("playlist_currently_open is dia")
                    back_arrow.draw()
                    open_list("dia", global_list_num)
                    draw_songs()
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
    if load_pause_once == True:
        if pause_or_play == "pause":
            pause_button.draw()
        if pause_or_play == "play":
            play_button.draw()

# This function draws the song names and rectangles which hold the song names
# when a playlist is opened.
def draw_songs():
    global current_scene
    global scroll
    global max_scroll
    global song_name_1
    global song_name_2
    global song_name_3
    global song_name_4
    global song_name_5
    global song_name_6
    global song_name_7
    global song_name_8
    global song_name_9
    if current_scene == "halloween":
        max_scroll = 3
        screen.draw.text(
            str(playlist_that_is_currently_open),
            midtop=(400, 50),
            fontsize=50,
            color="yellow",
        )
        screen.draw.rect(music_frame, "brown")

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

        scroll_up.draw()
        scroll_down.draw()

    if current_scene == "dia":
        max_scroll = 1
        screen.draw.text(
            str(playlist_that_is_currently_open),
            midtop=(400, 50),
            fontsize=50,
            color="pink",
        )
        screen.draw.rect(music_frame, "brown")

        screen.draw.text(song_name_1, (130, 130), fontsize=30, color="black")
        screen.draw.rect(dia_frame_1, "brown")

        screen.draw.text(song_name_2, (130, 170), fontsize=30, color="black")
        screen.draw.rect(dia_frame_2, "brown")

        screen.draw.text(song_name_3, (130, 210), fontsize=30, color="black")
        screen.draw.rect(dia_frame_3, "brown")

        screen.draw.text(song_name_4, (130, 250), fontsize=30, color="black")
        screen.draw.rect(dia_frame_4, "brown")

        screen.draw.text(song_name_5, (130, 290), fontsize=30, color="black")
        screen.draw.rect(dia_frame_5, "brown")

        screen.draw.text(song_name_6, (130, 330), fontsize=30, color="black")
        screen.draw.rect(dia_frame_6, "brown")

        screen.draw.text(song_name_7, (130, 370), fontsize=30, color="black")
        screen.draw.rect(dia_frame_7, "brown")

        screen.draw.text(song_name_8, (130, 410), fontsize=30, color="black")
        screen.draw.rect(dia_frame_8, "brown")

        screen.draw.text(song_name_9, (130, 450), fontsize=30, color="black")
        screen.draw.rect(dia_frame_9, "brown")

        screen.draw.text(song_name_10, (130, 490), fontsize=30, color="black")
        screen.draw.rect(dia_frame_10, "brown")

        scroll_up.draw()
        scroll_down.draw()

    if current_scene == "rosh":
        max_scroll = 1
        screen.draw.text(
            str(playlist_that_is_currently_open),
            midtop=(400, 50),
            fontsize=50,
            color="black",
        )
        screen.draw.rect(music_frame, "black")

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

        scroll_up.draw()
        scroll_down.draw()

# This function and the two below just change the scene 
# (kind of unnecessary but why fix what ain't broke?)
def start_halloween():
    global current_scene
    current_scene = "halloween"


def start_rosh():
    global current_scene
    current_scene = "rosh"


def start_dia():
    global current_scene
    current_scene = "dia"

# This function draws the playlist symbols with the proper names depending on the holiday
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

# this function names the lists depending on the holiday open. It's called every frame under update()
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
        play_name_1 = "Party"
        play_name_2 = "Spooky"
        play_name_3 = "Classical"
        play_name_4 = "Jumpscares"
        play_name_5 = "Rock and Roll"
        play_name_6 = "Jazz"
        play_name_7 = "Classics"
        play_name_8 = "For Kids"

    if current_scene == "dia":
        play_name_1 = "Celebration"
        play_name_2 = "Coco"
        play_name_3 = "Classics"
        play_name_4 = "Party"
        play_name_5 = "For Kids"
        play_name_6 = "dia_6"
        play_name_7 = "dia_7"
        play_name_8 = "dia_8"

    if current_scene == "rosh":
        play_name_1 = "Celebration"
        play_name_2 = "Religious"
        play_name_3 = "Party"
        play_name_4 = "For Kids"
        play_name_5 = "For Kids #2"
        play_name_6 = "rosh_6"
        play_name_7 = "rosh_7"
        play_name_8 = "rosh_8"

# This function defines what list is open and changes the songnames
# to corrospond with what list is being opened.
def open_list(list_holiday, playlist_num):
    global max_scroll
    global scroll
    global current_scene
    global playlist_currently_open
    global halloween_frame_1
    global halloween_frame_2
    global halloween_frame_3
    global halloween_frame_4
    global halloween_frame_5
    global halloween_frame_6
    global halloween_frame_7
    global halloween_frame_8
    global halloween_frame_9
    global halloween_frame_10
    global dia_frame_1
    global dia_frame_2
    global dia_frame_3
    global dia_frame_4
    global dia_frame_5
    global dia_frame_6
    global dia_frame_7
    global dia_frame_8
    global dia_frame_9
    global dia_frame_10
    global is_playlist_currently_open
    global playlist_that_is_currently_open
    global global_list_holiday
    global global_list_num
    is_playlist_currently_open = True
    if list_holiday == "halloween":
        global_list_holiday = "halloween"
        if playlist_num == 1:
            playlist_that_is_currently_open = "Party"
            global_list_num = 1
            load_songs("halloween", 1)
        if playlist_num == 2:
            playlist_that_is_currently_open = "Spooky"
            global_list_num = 2
            load_songs("halloween", 2)
        if playlist_num == 3:
            playlist_that_is_currently_open = "Classical"
            global_list_num = 3
            load_songs("halloween", 3)
        if playlist_num == 4:
            playlist_that_is_currently_open = "Jumpscares"
            global_list_num = 4
            load_songs("halloween", 4)
        if playlist_num == 5:
            playlist_that_is_currently_open = "Rock and Roll"
            global_list_num = 5
            load_songs("halloween", 5)
        if playlist_num == 6:
            playlist_that_is_currently_open = "Jazz"
            global_list_num = 6
            load_songs("halloween", 6)
        if playlist_num == 7:
            playlist_that_is_currently_open = "Classics"
            global_list_num = 7
            load_songs("halloween", 7)
        if playlist_num == 8:
            playlist_that_is_currently_open = "For Kids"
            global_list_num = 8
            load_songs("halloween", 8)
        playlist_currently_open = "halloween"

    if list_holiday == "dia":
        global_list_holiday = "dia"
        if playlist_num == 1:
            playlist_that_is_currently_open = "Celebration"
            global_list_num = 1
            load_songs("dia", 1)
        if playlist_num == 2:
            playlist_that_is_currently_open = "Coco"
            global_list_num = 2
            load_songs("dia", 2)
        if playlist_num == 3:
            playlist_that_is_currently_open = "Classics"
            global_list_num = 3
            load_songs("dia", 3)
        if playlist_num == 4:
            playlist_that_is_currently_open = "Party"
            global_list_num = 4
            load_songs("dia", 4)
        if playlist_num == 5:
            playlist_that_is_currently_open = "For Kids"
            global_list_num = 5
            load_songs("dia", 5)
        if playlist_num == 6:
            playlist_that_is_currently_open = "This playlist doesn't exist yet"
            global_list_num = 6
            load_songs("dia", 6)
        if playlist_num == 7:
            playlist_that_is_currently_open = "This playlist doesn't exist yet"
            global_list_num = 7
            load_songs("dia", 7)
        if playlist_num == 8:
            playlist_that_is_currently_open = "This playlist doesn't exist yet"
            global_list_num = 8
            load_songs("dia", 8)
        playlist_currently_open = "dia"

    if list_holiday == "rosh":
        global_list_holiday = "rosh"
        if playlist_num == 1:
            playlist_that_is_currently_open = "Celebration"
            global_list_num = 1
            load_songs("rosh", 1)
        if playlist_num == 2:
            playlist_that_is_currently_open = "Religious"
            global_list_num = 2
            load_songs("rosh", 2)
        if playlist_num == 3:
            playlist_that_is_currently_open = "Party"
            global_list_num = 3
            load_songs("rosh", 3)
        if playlist_num == 4:
            playlist_that_is_currently_open = "For Kids"
            global_list_num = 4
            load_songs("rosh", 4)
        if playlist_num == 5:
            playlist_that_is_currently_open = "For Kids #2"
            global_list_num = 5
            load_songs("rosh", 5)
        if playlist_num == 6:
            playlist_that_is_currently_open = "This Playlist Doesn't Exist Yet"
            global_list_num = 6
            load_songs("rosh", 6)
        if playlist_num == 7:
            playlist_that_is_currently_open = "This Playlist Doesn't Exist Yet"
            global_list_num = 7
            load_songs("rosh", 7)
        if playlist_num == 8:
            playlist_that_is_currently_open = "This Playlist Doesn't Exist Yet"
            global_list_num = 8
            load_songs("rosh", 8)
        playlist_currently_open = "rosh"


# This function figures out song names based on holiday, playlist and scroll
def load_songs(ls_holiday, ls_playlist_num):
    global song_name_1
    global song_name_2
    global song_name_3
    global song_name_4
    global song_name_5
    global song_name_6
    global song_name_7
    global song_name_8
    global song_name_9
    global song_name_10
    global scroll
    if ls_holiday == "halloween":
        if ls_playlist_num == 1:
            if scroll == 0:
                song_name_1 = "Ghostbusters Theme"
                song_name_2 = "Thriller"
                song_name_3 = "This is Halloween"
                song_name_4 = "halloween, list_1, sn4"
                song_name_5 = "halloween, list_1, sn5"
                song_name_6 = "halloween, list_1, sn6"
                song_name_7 = "halloween, list_1, sn7"
                song_name_8 = "halloween, list_1, sn8"
                song_name_9 = "halloween, list_1, sn9"
                song_name_10 = "halloween, list_1, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_1, sn11"
                song_name_2 = "halloween, list_1, sn12"
                song_name_3 = "halloween, list_1, sn13"
                song_name_4 = "halloween, list_1, sn14"
                song_name_5 = "halloween, list_1, sn15"
                song_name_6 = "halloween, list_1, sn16"
                song_name_7 = "halloween, list_1, sn17"
                song_name_8 = "halloween, list_1, sn18"
                song_name_9 = "halloween, list_1, sn19"
                song_name_10 = "halloween, list_1, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_1, sn21"
                song_name_2 = "halloween, list_1, sn22"
                song_name_3 = "halloween, list_1, sn23"
                song_name_4 = "halloween, list_1, sn24"
                song_name_5 = "halloween, list_1, sn25"
                song_name_6 = "halloween, list_1, sn26"
                song_name_7 = "halloween, list_1, sn27"
                song_name_8 = "halloween, list_1, sn28"
                song_name_9 = "halloween, list_1, sn29"
                song_name_10 = "halloween, list_1, sn30"

        if ls_playlist_num == 2:
            if scroll == 0:
                song_name_1 = "halloween, list_2, sn1"
                song_name_2 = "halloween, list_2, sn2"
                song_name_3 = "halloween, list_2, sn3"
                song_name_4 = "halloween, list_2, sn4"
                song_name_5 = "halloween, list_2, sn5"
                song_name_6 = "halloween, list_2, sn6"
                song_name_7 = "halloween, list_2, sn7"
                song_name_8 = "halloween, list_2, sn8"
                song_name_9 = "halloween, list_2, sn9"
                song_name_10 = "halloween, list_2, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_2, sn11"
                song_name_2 = "halloween, list_2, sn12"
                song_name_3 = "halloween, list_2, sn13"
                song_name_4 = "halloween, list_2, sn14"
                song_name_5 = "halloween, list_2, sn15"
                song_name_6 = "halloween, list_2, sn16"
                song_name_7 = "halloween, list_2, sn17"
                song_name_8 = "halloween, list_2, sn18"
                song_name_9 = "halloween, list_2, sn19"
                song_name_10 = "halloween, list_2, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_2, sn21"
                song_name_2 = "halloween, list_2, sn22"
                song_name_3 = "halloween, list_2, sn23"
                song_name_4 = "halloween, list_2, sn24"
                song_name_5 = "halloween, list_2, sn25"
                song_name_6 = "halloween, list_2, sn26"
                song_name_7 = "halloween, list_2, sn27"
                song_name_8 = "halloween, list_2, sn28"
                song_name_9 = "halloween, list_2, sn29"
                song_name_10 = "halloween, list_2, sn30"

        if ls_playlist_num == 3:
            if scroll == 0:
                song_name_1 = "halloween, list_3, sn1"
                song_name_2 = "halloween, list_3, sn2"
                song_name_3 = "halloween, list_3, sn3"
                song_name_4 = "halloween, list_3, sn4"
                song_name_5 = "halloween, list_3, sn5"
                song_name_6 = "halloween, list_3, sn6"
                song_name_7 = "halloween, list_3, sn7"
                song_name_8 = "halloween, list_3, sn8"
                song_name_9 = "halloween, list_3, sn9"
                song_name_10 = "halloween, list_3, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_3, sn11"
                song_name_2 = "halloween, list_3, sn12"
                song_name_3 = "halloween, list_3, sn13"
                song_name_4 = "halloween, list_3, sn14"
                song_name_5 = "halloween, list_3, sn15"
                song_name_6 = "halloween, list_3, sn16"
                song_name_7 = "halloween, list_3, sn17"
                song_name_8 = "halloween, list_3, sn18"
                song_name_9 = "halloween, list_3, sn19"
                song_name_10 = "halloween, list_3, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_3, sn21"
                song_name_2 = "halloween, list_3, sn22"
                song_name_3 = "halloween, list_3, sn23"
                song_name_4 = "halloween, list_3, sn24"
                song_name_5 = "halloween, list_3, sn25"
                song_name_6 = "halloween, list_3, sn26"
                song_name_7 = "halloween, list_3, sn27"
                song_name_8 = "halloween, list_3, sn28"
                song_name_9 = "halloween, list_3, sn29"
                song_name_10 = "halloween, list_3, sn30"

        if ls_playlist_num == 4:
            if scroll == 0:
                song_name_1 = "halloween, list_4, sn1"
                song_name_2 = "halloween, list_4, sn2"
                song_name_3 = "halloween, list_4, sn3"
                song_name_4 = "halloween, list_4, sn4"
                song_name_5 = "halloween, list_4, sn5"
                song_name_6 = "halloween, list_4, sn6"
                song_name_7 = "halloween, list_4, sn7"
                song_name_8 = "halloween, list_4, sn8"
                song_name_9 = "halloween, list_4, sn9"
                song_name_10 = "halloween, list_4, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_4, sn11"
                song_name_2 = "halloween, list_4, sn12"
                song_name_3 = "halloween, list_4, sn13"
                song_name_4 = "halloween, list_4, sn14"
                song_name_5 = "halloween, list_4, sn15"
                song_name_6 = "halloween, list_4, sn16"
                song_name_7 = "halloween, list_4, sn17"
                song_name_8 = "halloween, list_4, sn18"
                song_name_9 = "halloween, list_4, sn19"
                song_name_10 = "halloween, list_4, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_4, sn21"
                song_name_2 = "halloween, list_4, sn22"
                song_name_3 = "halloween, list_4, sn23"
                song_name_4 = "halloween, list_4, sn24"
                song_name_5 = "halloween, list_4, sn25"
                song_name_6 = "halloween, list_4, sn26"
                song_name_7 = "halloween, list_4, sn27"
                song_name_8 = "halloween, list_4, sn28"
                song_name_9 = "halloween, list_4, sn29"
                song_name_10 = "halloween, list_4, sn30"

        if ls_playlist_num == 5:
            if scroll == 0:
                song_name_1 = "halloween, list_5, sn1"
                song_name_2 = "halloween, list_5, sn2"
                song_name_3 = "halloween, list_5, sn3"
                song_name_4 = "halloween, list_5, sn4"
                song_name_5 = "halloween, list_5, sn5"
                song_name_6 = "halloween, list_5, sn6"
                song_name_7 = "halloween, list_5, sn7"
                song_name_8 = "halloween, list_5, sn8"
                song_name_9 = "halloween, list_5, sn9"
                song_name_10 = "halloween, list_5, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_5, sn11"
                song_name_2 = "halloween, list_5, sn12"
                song_name_3 = "halloween, list_5, sn13"
                song_name_4 = "halloween, list_5, sn14"
                song_name_5 = "halloween, list_5, sn15"
                song_name_6 = "halloween, list_5, sn16"
                song_name_7 = "halloween, list_5, sn17"
                song_name_8 = "halloween, list_5, sn18"
                song_name_9 = "halloween, list_5, sn19"
                song_name_10 = "halloween, list_5, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_5, sn21"
                song_name_2 = "halloween, list_5, sn22"
                song_name_3 = "halloween, list_5, sn23"
                song_name_4 = "halloween, list_5, sn24"
                song_name_5 = "halloween, list_5, sn25"
                song_name_6 = "halloween, list_5, sn26"
                song_name_7 = "halloween, list_5, sn27"
                song_name_8 = "halloween, list_5, sn28"
                song_name_9 = "halloween, list_5, sn29"
                song_name_10 = "halloween, list_5, sn30"

        if ls_playlist_num == 6:
            if scroll == 0:
                song_name_1 = "halloween, list_6, sn1"
                song_name_2 = "halloween, list_6, sn2"
                song_name_3 = "halloween, list_6, sn3"
                song_name_4 = "halloween, list_6, sn4"
                song_name_5 = "halloween, list_6, sn5"
                song_name_6 = "halloween, list_6, sn6"
                song_name_7 = "halloween, list_6, sn7"
                song_name_8 = "halloween, list_6, sn8"
                song_name_9 = "halloween, list_6, sn9"
                song_name_10 = "halloween, list_6, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_6, sn11"
                song_name_2 = "halloween, list_6, sn12"
                song_name_3 = "halloween, list_6, sn13"
                song_name_4 = "halloween, list_6, sn14"
                song_name_5 = "halloween, list_6, sn15"
                song_name_6 = "halloween, list_6, sn16"
                song_name_7 = "halloween, list_6, sn17"
                song_name_8 = "halloween, list_6, sn18"
                song_name_9 = "halloween, list_6, sn19"
                song_name_10 = "halloween, list_6, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_6, sn21"
                song_name_2 = "halloween, list_6, sn22"
                song_name_3 = "halloween, list_6, sn23"
                song_name_4 = "halloween, list_6, sn24"
                song_name_5 = "halloween, list_6, sn25"
                song_name_6 = "halloween, list_6, sn26"
                song_name_7 = "halloween, list_6, sn27"
                song_name_8 = "halloween, list_6, sn28"
                song_name_9 = "halloween, list_6, sn29"
                song_name_10 = "halloween, list_6, sn30"

        if ls_playlist_num == 7:
            if scroll == 0:
                song_name_1 = "halloween, list_7, sn1"
                song_name_2 = "halloween, list_7, sn2"
                song_name_3 = "halloween, list_7, sn3"
                song_name_4 = "halloween, list_7, sn4"
                song_name_5 = "halloween, list_7, sn5"
                song_name_6 = "halloween, list_7, sn6"
                song_name_7 = "halloween, list_7, sn7"
                song_name_8 = "halloween, list_7, sn8"
                song_name_9 = "halloween, list_7, sn9"
                song_name_10 = "halloween, list_7, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_7, sn11"
                song_name_2 = "halloween, list_7, sn12"
                song_name_3 = "halloween, list_7, sn13"
                song_name_4 = "halloween, list_7, sn14"
                song_name_5 = "halloween, list_7, sn15"
                song_name_6 = "halloween, list_7, sn16"
                song_name_7 = "halloween, list_7, sn17"
                song_name_8 = "halloween, list_7, sn18"
                song_name_9 = "halloween, list_7, sn19"
                song_name_10 = "halloween, list_7, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_7, sn21"
                song_name_2 = "halloween, list_7, sn22"
                song_name_3 = "halloween, list_7, sn23"
                song_name_4 = "halloween, list_7, sn24"
                song_name_5 = "halloween, list_7, sn25"
                song_name_6 = "halloween, list_7, sn26"
                song_name_7 = "halloween, list_7, sn27"
                song_name_8 = "halloween, list_7, sn28"
                song_name_9 = "halloween, list_7, sn29"
                song_name_10 = "halloween, list_7, sn30"

        if ls_playlist_num == 8:
            if scroll == 0:
                song_name_1 = "halloween, list_8, sn1"
                song_name_2 = "halloween, list_8, sn2"
                song_name_3 = "halloween, list_8, sn3"
                song_name_4 = "halloween, list_8, sn4"
                song_name_5 = "halloween, list_8, sn5"
                song_name_6 = "halloween, list_8, sn6"
                song_name_7 = "halloween, list_8, sn7"
                song_name_8 = "halloween, list_8, sn8"
                song_name_9 = "halloween, list_8, sn9"
                song_name_10 = "halloween, list_8, sn10"
            if scroll == 1:
                song_name_1 = "halloween, list_8, sn11"
                song_name_2 = "halloween, list_8, sn12"
                song_name_3 = "halloween, list_8, sn13"
                song_name_4 = "halloween, list_8, sn14"
                song_name_5 = "halloween, list_8, sn15"
                song_name_6 = "halloween, list_8, sn16"
                song_name_7 = "halloween, list_8, sn17"
                song_name_8 = "halloween, list_8, sn18"
                song_name_9 = "halloween, list_8, sn19"
                song_name_10 = "halloween, list_8, sn20"
            if scroll == 2:
                song_name_1 = "halloween, list_8, sn21"
                song_name_2 = "halloween, list_8, sn22"
                song_name_3 = "halloween, list_8, sn23"
                song_name_4 = "halloween, list_8, sn24"
                song_name_5 = "halloween, list_8, sn25"
                song_name_6 = "halloween, list_8, sn26"
                song_name_7 = "halloween, list_8, sn27"
                song_name_8 = "halloween, list_8, sn28"
                song_name_9 = "halloween, list_8, sn29"
                song_name_10 = "halloween, list_8, sn30"
    if ls_holiday == "dia":
        if ls_playlist_num == 1:
            if scroll == 0:
                song_name_1 = "dia, list_1, sn1"
                song_name_2 = "dia, list_1, sn2"
                song_name_3 = "dia, list_1, sn3"
                song_name_4 = "dia, list_1, sn4"
                song_name_5 = "dia, list_1, sn5"
                song_name_6 = "dia, list_1, sn6"
                song_name_7 = "dia, list_1, sn7"
                song_name_8 = "dia, list_1, sn8"
                song_name_9 = "dia, list_1, sn9"
                song_name_10 = "dia, list_1, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_1, sn11"
                song_name_2 = "dia, list_1, sn12"
                song_name_3 = "dia, list_1, sn13"
                song_name_4 = "dia, list_1, sn14"
                song_name_5 = "dia, list_1, sn15"
                song_name_6 = "dia, list_1, sn16"
                song_name_7 = "dia, list_1, sn17"
                song_name_8 = "dia, list_1, sn18"
                song_name_9 = "dia, list_1, sn19"
                song_name_10 = "dia, list_1, sn20"
        if ls_playlist_num == 2:
            if scroll == 0:
                song_name_1 = "dia, list_2, sn1"
                song_name_2 = "dia, list_2, sn2"
                song_name_3 = "dia, list_2, sn3"
                song_name_4 = "dia, list_2, sn4"
                song_name_5 = "dia, list_2, sn5"
                song_name_6 = "dia, list_2, sn6"
                song_name_7 = "dia, list_2, sn7"
                song_name_8 = "dia, list_2, sn8"
                song_name_9 = "dia, list_2, sn9"
                song_name_10 = "dia, list_2, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_2, sn11"
                song_name_2 = "dia, list_2, sn12"
                song_name_3 = "dia, list_2, sn13"
                song_name_4 = "dia, list_2, sn14"
                song_name_5 = "dia, list_2, sn15"
                song_name_6 = "dia, list_2, sn16"
                song_name_7 = "dia, list_2, sn17"
                song_name_8 = "dia, list_2, sn18"
                song_name_9 = "dia, list_2, sn19"
                song_name_10 = "dia, list_2, sn20"
        if ls_playlist_num == 3:
            if scroll == 0:
                song_name_1 = "dia, list_3, sn1"
                song_name_2 = "dia, list_3, sn2"
                song_name_3 = "dia, list_3, sn3"
                song_name_4 = "dia, list_3, sn4"
                song_name_5 = "dia, list_3, sn5"
                song_name_6 = "dia, list_3, sn6"
                song_name_7 = "dia, list_3, sn7"
                song_name_8 = "dia, list_3, sn8"
                song_name_9 = "dia, list_3, sn9"
                song_name_10 = "dia, list_3, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_3, sn11"
                song_name_2 = "dia, list_3, sn12"
                song_name_3 = "dia, list_3, sn13"
                song_name_4 = "dia, list_3, sn14"
                song_name_5 = "dia, list_3, sn15"
                song_name_6 = "dia, list_3, sn16"
                song_name_7 = "dia, list_3, sn17"
                song_name_8 = "dia, list_3, sn18"
                song_name_9 = "dia, list_3, sn19"
                song_name_10 = "dia, list_3, sn20"
        if ls_playlist_num == 4:
            if scroll == 0:
                song_name_1 = "dia, list_4, sn1"
                song_name_2 = "dia, list_4, sn2"
                song_name_3 = "dia, list_4, sn3"
                song_name_4 = "dia, list_4, sn4"
                song_name_5 = "dia, list_4, sn5"
                song_name_6 = "dia, list_4, sn6"
                song_name_7 = "dia, list_4, sn7"
                song_name_8 = "dia, list_4, sn8"
                song_name_9 = "dia, list_4, sn9"
                song_name_10 = "dia, list_4, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_4, sn11"
                song_name_2 = "dia, list_4, sn12"
                song_name_3 = "dia, list_4, sn13"
                song_name_4 = "dia, list_4, sn14"
                song_name_5 = "dia, list_4, sn15"
                song_name_6 = "dia, list_4, sn16"
                song_name_7 = "dia, list_4, sn17"
                song_name_8 = "dia, list_4, sn18"
                song_name_9 = "dia, list_4, sn19"
                song_name_10 = "dia, list_4, sn20"
        if ls_playlist_num == 5:
            if scroll == 0:
                song_name_1 = "dia, list_5, sn1"
                song_name_2 = "dia, list_5, sn2"
                song_name_3 = "dia, list_5, sn3"
                song_name_4 = "dia, list_5, sn4"
                song_name_5 = "dia, list_5, sn5"
                song_name_6 = "dia, list_5, sn6"
                song_name_7 = "dia, list_5, sn7"
                song_name_8 = "dia, list_5, sn8"
                song_name_9 = "dia, list_5, sn9"
                song_name_10 = "dia, list_5, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_5, sn11"
                song_name_2 = "dia, list_5, sn12"
                song_name_3 = "dia, list_5, sn13"
                song_name_4 = "dia, list_5, sn14"
                song_name_5 = "dia, list_5, sn15"
                song_name_6 = "dia, list_5, sn16"
                song_name_7 = "dia, list_5, sn17"
                song_name_8 = "dia, list_5, sn18"
                song_name_9 = "dia, list_5, sn19"
                song_name_10 = "dia, list_5, sn20"
        if ls_playlist_num == 6:
            if scroll == 0:
                song_name_1 = "dia, list_6, sn1"
                song_name_2 = "dia, list_6, sn2"
                song_name_3 = "dia, list_6, sn3"
                song_name_4 = "dia, list_6, sn4"
                song_name_5 = "dia, list_6, sn5"
                song_name_6 = "dia, list_6, sn6"
                song_name_7 = "dia, list_6, sn7"
                song_name_8 = "dia, list_6, sn8"
                song_name_9 = "dia, list_6, sn9"
                song_name_10 = "dia, list_6, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_6, sn11"
                song_name_2 = "dia, list_6, sn12"
                song_name_3 = "dia, list_6, sn13"
                song_name_4 = "dia, list_6, sn14"
                song_name_5 = "dia, list_6, sn15"
                song_name_6 = "dia, list_6, sn16"
                song_name_7 = "dia, list_6, sn17"
                song_name_8 = "dia, list_6, sn18"
                song_name_9 = "dia, list_6, sn19"
                song_name_10 = "dia, list_6, sn20"
        if ls_playlist_num == 7:
            if scroll == 0:
                song_name_1 = "dia, list_7, sn1"
                song_name_2 = "dia, list_7, sn2"
                song_name_3 = "dia, list_7, sn3"
                song_name_4 = "dia, list_7, sn4"
                song_name_5 = "dia, list_7, sn5"
                song_name_6 = "dia, list_7, sn6"
                song_name_7 = "dia, list_7, sn7"
                song_name_8 = "dia, list_7, sn8"
                song_name_9 = "dia, list_7, sn9"
                song_name_10 = "dia, list_7, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_7, sn11"
                song_name_2 = "dia, list_7, sn12"
                song_name_3 = "dia, list_7, sn13"
                song_name_4 = "dia, list_7, sn14"
                song_name_5 = "dia, list_7, sn15"
                song_name_6 = "dia, list_7, sn16"
                song_name_7 = "dia, list_7, sn17"
                song_name_8 = "dia, list_7, sn18"
                song_name_9 = "dia, list_7, sn19"
                song_name_10 = "dia, list_7, sn20"
        if ls_playlist_num == 8:
            if scroll == 0:
                song_name_1 = "dia, list_8, sn1"
                song_name_2 = "dia, list_8, sn2"
                song_name_3 = "dia, list_8, sn3"
                song_name_4 = "dia, list_8, sn4"
                song_name_5 = "dia, list_8, sn5"
                song_name_6 = "dia, list_8, sn6"
                song_name_7 = "dia, list_8, sn7"
                song_name_8 = "dia, list_8, sn8"
                song_name_9 = "dia, list_8, sn9"
                song_name_10 = "dia, list_8, sn10"
            if scroll == 1:
                song_name_1 = "dia, list_8, sn11"
                song_name_2 = "dia, list_8, sn12"
                song_name_3 = "dia, list_8, sn13"
                song_name_4 = "dia, list_8, sn14"
                song_name_5 = "dia, list_8, sn15"
                song_name_6 = "dia, list_8, sn16"
                song_name_7 = "dia, list_8, sn17"
                song_name_8 = "dia, list_8, sn18"
                song_name_9 = "dia, list_8, sn19"
                song_name_10 = "dia, list_8, sn20"
    if ls_holiday == "rosh":
        if ls_playlist_num == 1:
            if scroll == 0:
                song_name_1 = "rosh, list_1, sn1"
                song_name_2 = "rosh, list_1, sn2"
                song_name_3 = "rosh, list_1, sn3"
                song_name_4 = "rosh, list_1, sn4"
                song_name_5 = "rosh, list_1, sn5"
                song_name_6 = "rosh, list_1, sn6"
                song_name_7 = "rosh, list_1, sn7"
                song_name_8 = "rosh, list_1, sn8"
                song_name_9 = "rosh, list_1, sn9"
                song_name_10 = "rosh, list_1, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_1, sn11"
                song_name_2 = "rosh, list_1, sn12"
                song_name_3 = "rosh, list_1, sn13"
                song_name_4 = "rosh, list_1, sn14"
                song_name_5 = "rosh, list_1, sn15"
                song_name_6 = "rosh, list_1, sn16"
                song_name_7 = "rosh, list_1, sn17"
                song_name_8 = "rosh, list_1, sn18"
                song_name_9 = "rosh, list_1, sn19"
                song_name_10 = "rosh, list_1, sn20"
        if ls_playlist_num == 2:
            if scroll == 0:
                song_name_1 = "rosh, list_2, sn1"
                song_name_2 = "rosh, list_2, sn2"
                song_name_3 = "rosh, list_2, sn3"
                song_name_4 = "rosh, list_2, sn4"
                song_name_5 = "rosh, list_2, sn5"
                song_name_6 = "rosh, list_2, sn6"
                song_name_7 = "rosh, list_2, sn7"
                song_name_8 = "rosh, list_2, sn8"
                song_name_9 = "rosh, list_2, sn9"
                song_name_10 = "rosh, list_2, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_2, sn11"
                song_name_2 = "rosh, list_2, sn12"
                song_name_3 = "rosh, list_2, sn13"
                song_name_4 = "rosh, list_2, sn14"
                song_name_5 = "rosh, list_2, sn15"
                song_name_6 = "rosh, list_2, sn16"
                song_name_7 = "rosh, list_2, sn17"
                song_name_8 = "rosh, list_2, sn18"
                song_name_9 = "rosh, list_2, sn19"
                song_name_10 = "rosh, list_2, sn20"
        if ls_playlist_num == 3:
            if scroll == 0:
                song_name_1 = "rosh, list_3, sn1"
                song_name_2 = "rosh, list_3, sn2"
                song_name_3 = "rosh, list_3, sn3"
                song_name_4 = "rosh, list_3, sn4"
                song_name_5 = "rosh, list_3, sn5"
                song_name_6 = "rosh, list_3, sn6"
                song_name_7 = "rosh, list_3, sn7"
                song_name_8 = "rosh, list_3, sn8"
                song_name_9 = "rosh, list_3, sn9"
                song_name_10 = "rosh, list_3, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_3, sn11"
                song_name_2 = "rosh, list_3, sn12"
                song_name_3 = "rosh, list_3, sn13"
                song_name_4 = "rosh, list_3, sn14"
                song_name_5 = "rosh, list_3, sn15"
                song_name_6 = "rosh, list_3, sn16"
                song_name_7 = "rosh, list_3, sn17"
                song_name_8 = "rosh, list_3, sn18"
                song_name_9 = "rosh, list_3, sn19"
                song_name_10 = "rosh, list_3, sn20"
        if ls_playlist_num == 4:
            if scroll == 0:
                song_name_1 = "rosh, list_4, sn1"
                song_name_2 = "rosh, list_4, sn2"
                song_name_3 = "rosh, list_4, sn3"
                song_name_4 = "rosh, list_4, sn4"
                song_name_5 = "rosh, list_4, sn5"
                song_name_6 = "rosh, list_4, sn6"
                song_name_7 = "rosh, list_4, sn7"
                song_name_8 = "rosh, list_4, sn8"
                song_name_9 = "rosh, list_4, sn9"
                song_name_10 = "rosh, list_4, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_4, sn11"
                song_name_2 = "rosh, list_4, sn12"
                song_name_3 = "rosh, list_4, sn13"
                song_name_4 = "rosh, list_4, sn14"
                song_name_5 = "rosh, list_4, sn15"
                song_name_6 = "rosh, list_4, sn16"
                song_name_7 = "rosh, list_4, sn17"
                song_name_8 = "rosh, list_4, sn18"
                song_name_9 = "rosh, list_4, sn19"
                song_name_10 = "rosh, list_4, sn20"
        if ls_playlist_num == 5:
            if scroll == 0:
                song_name_1 = "rosh, list_5, sn1"
                song_name_2 = "rosh, list_5, sn2"
                song_name_3 = "rosh, list_5, sn3"
                song_name_4 = "rosh, list_5, sn4"
                song_name_5 = "rosh, list_5, sn5"
                song_name_6 = "rosh, list_5, sn6"
                song_name_7 = "rosh, list_5, sn7"
                song_name_8 = "rosh, list_5, sn8"
                song_name_9 = "rosh, list_5, sn9"
                song_name_10 = "rosh, list_5, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_5, sn11"
                song_name_2 = "rosh, list_5, sn12"
                song_name_3 = "rosh, list_5, sn13"
                song_name_4 = "rosh, list_5, sn14"
                song_name_5 = "rosh, list_5, sn15"
                song_name_6 = "rosh, list_5, sn16"
                song_name_7 = "rosh, list_5, sn17"
                song_name_8 = "rosh, list_5, sn18"
                song_name_9 = "rosh, list_5, sn19"
                song_name_10 = "rosh, list_5, sn20"
        if ls_playlist_num == 6:
            if scroll == 0:
                song_name_1 = "rosh, list_6, sn1"
                song_name_2 = "rosh, list_6, sn2"
                song_name_3 = "rosh, list_6, sn3"
                song_name_4 = "rosh, list_6, sn4"
                song_name_5 = "rosh, list_6, sn5"
                song_name_6 = "rosh, list_6, sn6"
                song_name_7 = "rosh, list_6, sn7"
                song_name_8 = "rosh, list_6, sn8"
                song_name_9 = "rosh, list_6, sn9"
                song_name_10 = "rosh, list_6, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_6, sn11"
                song_name_2 = "rosh, list_6, sn12"
                song_name_3 = "rosh, list_6, sn13"
                song_name_4 = "rosh, list_6, sn14"
                song_name_5 = "rosh, list_6, sn15"
                song_name_6 = "rosh, list_6, sn16"
                song_name_7 = "rosh, list_6, sn17"
                song_name_8 = "rosh, list_6, sn18"
                song_name_9 = "rosh, list_6, sn19"
                song_name_10 = "rosh, list_6, sn20"
        if ls_playlist_num == 7:
            if scroll == 0:
                song_name_1 = "rosh, list_7, sn1"
                song_name_2 = "rosh, list_7, sn2"
                song_name_3 = "rosh, list_7, sn3"
                song_name_4 = "rosh, list_7, sn4"
                song_name_5 = "rosh, list_7, sn5"
                song_name_6 = "rosh, list_7, sn6"
                song_name_7 = "rosh, list_7, sn7"
                song_name_8 = "rosh, list_7, sn8"
                song_name_9 = "rosh, list_7, sn9"
                song_name_10 = "rosh, list_7, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_7, sn11"
                song_name_2 = "rosh, list_7, sn12"
                song_name_3 = "rosh, list_7, sn13"
                song_name_4 = "rosh, list_7, sn14"
                song_name_5 = "rosh, list_7, sn15"
                song_name_6 = "rosh, list_7, sn16"
                song_name_7 = "rosh, list_7, sn17"
                song_name_8 = "rosh, list_7, sn18"
                song_name_9 = "rosh, list_7, sn19"
                song_name_10 = "rosh, list_7, sn20"
        if ls_playlist_num == 8:
            if scroll == 0:
                song_name_1 = "rosh, list_8, sn1"
                song_name_2 = "rosh, list_8, sn2"
                song_name_3 = "rosh, list_8, sn3"
                song_name_4 = "rosh, list_8, sn4"
                song_name_5 = "rosh, list_8, sn5"
                song_name_6 = "rosh, list_8, sn6"
                song_name_7 = "rosh, list_8, sn7"
                song_name_8 = "rosh, list_8, sn8"
                song_name_9 = "rosh, list_8, sn9"
                song_name_10 = "rosh, list_8, sn10"
            if scroll == 1:
                song_name_1 = "rosh, list_8, sn11"
                song_name_2 = "rosh, list_8, sn12"
                song_name_3 = "rosh, list_8, sn13"
                song_name_4 = "rosh, list_8, sn14"
                song_name_5 = "rosh, list_8, sn15"
                song_name_6 = "rosh, list_8, sn16"
                song_name_7 = "rosh, list_8, sn17"
                song_name_8 = "rosh, list_8, sn18"
                song_name_9 = "rosh, list_8, sn19"
                song_name_10 = "rosh, list_8, sn20"

# This function starts playing songs based on which music frame is clicked.
# It distinguishes between scenes and scrolls too.
def play_a_song(frame_num):
    global load_pause_once
    global current_scene
    global global_list_num
    global scroll
    load_pause_once = True
    if current_scene == "halloween":
        if is_playlist_currently_open == True:
            if global_list_num == 1:
                if scroll == 0:
                    if frame_num == 1:
                        # print("halloween song 1 is playing")
                        music.play_once("halloween1play1song1")
                    if frame_num == 2:
                        music.play_once("halloween1play1song2")
                        # print("halloween song 2 is playing")
                    if frame_num == 3:
                        music.play_once("halloween1play1song3")
                        # print("halloween song 3 is playing")

# This function pauses songs if a song is playing
def pause_song():
    if pause_or_play == "play":
        music.pause()
        print("music is paused")

# This function unpauses songs if a song isn't playing
def unpause_song():
    if pause_or_play == "pause":
        music.unpause()
        print("music is unpaused")

# This functin changes the scene to the tree room
def enter_tree_room():
    global current_scene
    current_scene = "tree_room"
    # music.play("treeroom")
    # FIXME make this let it grow chorus loop

# This function flips the tree image horizontally.
def fliptree():
    global treeside
    if treeside == 0:
        dancing_tree.draw()
        treeside = 1
    else:
        dancing_tree_opposite.draw()
        treeside = 0


# this function deals with whenever the mouse is clicked
# FIXME make sure playlists can't be opened right after the scene is changed, use update function
# with smth similar to what is in the update function already
def on_mouse_down(pos):
    global max_scroll
    global scroll
    global current_scene
    global is_playlist_currently_open
    global pause_or_play
    global waiting_on_mouse
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
            if is_playlist_currently_open == False:
                current_scene = "setup"
            if is_playlist_currently_open:
                is_playlist_currently_open = False
    if scroll_down.collidepoint(pos):
        if (
            current_scene == "halloween"
            or current_scene == "rosh"
            or current_scene == "dia"
        ):
            if scroll < max_scroll:
                scroll = scroll + 1
    if scroll_up.collidepoint(pos):
        if (
            current_scene == "halloween"
            or current_scene == "rosh"
            or current_scene == "dia"
        ):
            if scroll > 0:
                scroll = scroll - 1
    if playlist_symbol_1.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 1)
            if current_scene == "dia":
                open_list("dia", 1)
            if current_scene == "rosh":
                open_list("rosh", 1)
    if playlist_symbol_2.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 2)
            if current_scene == "dia":
                open_list("dia", 2)
            if current_scene == "rosh":
                open_list("rosh", 2)
    if playlist_symbol_3.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 3)
            if current_scene == "dia":
                open_list("dia", 3)
            if current_scene == "rosh":
                open_list("rosh", 3)
    if playlist_symbol_4.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 4)
            if current_scene == "dia":
                open_list("dia", 4)
            if current_scene == "rosh":
                open_list("rosh", 4)
    if playlist_symbol_5.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 5)
            if current_scene == "dia":
                open_list("dia", 5)
            if current_scene == "rosh":
                open_list("rosh", 5)
    if playlist_symbol_6.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 6)
            if current_scene == "dia":
                open_list("dia", 6)
            if current_scene == "rosh":
                open_list("rosh", 6)
    if playlist_symbol_7.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 7)
            if current_scene == "dia":
                open_list("dia", 7)
            if current_scene == "rosh":
                open_list("rosh", 7)
    if playlist_symbol_8.collidepoint(pos):
        if is_playlist_currently_open == False:
            if current_scene == "halloween":
                open_list("halloween", 8)
            if current_scene == "dia":
                open_list("dia", 8)
            if current_scene == "rosh":
                open_list("rosh", 8)
    if halloween_frame_1.collidepoint(pos):
        play_a_song(1)
    if pause_or_play == "pause" and pause_button.collidepoint(pos):
        pause_or_play = "play"
        pause_song()
    elif pause_or_play == "play" and play_button.collidepoint(pos):
        pause_or_play = "pause"
        unpause_song()
    if halloween_frame_2.collidepoint(pos):
        play_a_song(2)
    if halloween_frame_3.collidepoint(pos):
        play_a_song(3)


# this function is called every frame
def update():
    global current_scene
    global is_playlist_currently_open
    global waiting_on_escape
    name_lists()
    if keyboard[keys.ESCAPE]:
        waiting_on_escape = True
    if not keyboard[keys.ESCAPE] and waiting_on_escape:
        waiting_on_escape = False
        if current_scene in ["tree_room", "halloween", "rosh", "dia"]:
            if is_playlist_currently_open == False:
                current_scene = "setup"
            if is_playlist_currently_open:
                is_playlist_currently_open = False


# This has to be the last line in the program
pgzrun.go()
