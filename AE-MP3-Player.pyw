from tkinter import *
import pygame
from tkinter import filedialog
from pathlib import Path
from PIL import ImageTk, Image
import webbrowser
from tkinter.messagebox import showinfo
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root = Tk()
root.title('ArabEagles Mp3 Player')
root.iconbitmap('logo2.ico')
root.geometry("500x460")
root.resizable(width=False, height=False)
bgimage = ImageTk.PhotoImage(Image.open('titlelogo.png'))
Label(root, image = bgimage).place(relwidth = 1, relheight = 1)

# Initalize Pygame Mixer
pygame.mixer.init()

# Functions
# Add Song to playlist
def add_song():
    song = filedialog.askopenfilename(initialdir='C:/users/Public/Music/',title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # Add song to listbox
    song_box.insert(END, song)

# Add many songs to playlist
def add__many_song():
    songs = filedialog.askopenfilenames(initialdir='C:/users/Public/Music/',title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # Add songs to listbox
    for song in songs:
        song_box.insert(END, song)

# Play Selected Song
def play():
    # Set stopped variable to false so slider work again
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Call the play_time func. to get song duration
    play_time()

    # Get current volume
    current_volume = pygame.mixer.music.get_volume()
    # change time to be easier to work with volume meter
    current_volume = current_volume * 100
    # Change volume meter image
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 5:
        volume_meter.config(image=vol5)
    elif int(current_volume) > 5 and int(current_volume) <= 10:
        volume_meter.config(image=vol10)
    elif int(current_volume) > 10 and int(current_volume) <= 15:
        volume_meter.config(image=vol15)
    elif int(current_volume) > 15 and int(current_volume) <= 20:
        volume_meter.config(image=vol20)
    elif int(current_volume) > 20 and int(current_volume) <= 25:
        volume_meter.config(image=vol25)
    elif int(current_volume) > 25 and int(current_volume) <= 30:
        volume_meter.config(image=vol30)
    elif int(current_volume) > 30 and int(current_volume) <= 35:
        volume_meter.config(image=vol35)
    elif int(current_volume) > 35 and int(current_volume) <= 40:
        volume_meter.config(image=vol40)
    elif int(current_volume) > 40 and int(current_volume) <= 45:
        volume_meter.config(image=vol45)
    elif int(current_volume) > 45 and int(current_volume) <= 50:
        volume_meter.config(image=vol50)
    elif int(current_volume) > 50 and int(current_volume) <= 55:
        volume_meter.config(image=vol55)
    elif int(current_volume) > 55 and int(current_volume) <= 60:
        volume_meter.config(image=vol60)
    elif int(current_volume) > 60 and int(current_volume) <= 65:
        volume_meter.config(image=vol65)
    elif int(current_volume) > 65 and int(current_volume) <= 70:
        volume_meter.config(image=vol70)
    elif int(current_volume) > 70 and int(current_volume) <= 75:
        volume_meter.config(image=vol75)
    elif int(current_volume) > 75 and int(current_volume) <= 80:
        volume_meter.config(image=vol80)
    elif int(current_volume) > 80 and int(current_volume) <= 85:
        volume_meter.config(image=vol85)
    elif int(current_volume) > 85 and int(current_volume) <= 90:
        volume_meter.config(image=vol90)
    elif int(current_volume) > 90 and int(current_volume) <= 95:
        volume_meter.config(image=vol95)
    elif int(current_volume) > 95 and int(current_volume) <= 100:
        volume_meter.config(image=vol100)


# Stop Playing Current Song
global stopped
stopped = False
def stop():
    # Reset slider and duration bar
    dur_status.config(text='')
    my_slider.config(value=0)
    # Stop current playing song
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # Clear Duration status Bar
    dur_status.config(text='')

    # Set stop variable to True
    global stopped
    stopped = True

# Create Global Pause Variable
global paused
paused = False

# Pause and Unpause the Current Song
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # Unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # Pause
        pygame.mixer.music.pause()
        paused = True

# Play the next song in the playlist
def next_song():
    # Reset slider and duration bar
    dur_status.config(text='')
    my_slider.config(value=0)
    # Get the current song listed number
    next_one = song_box.curselection()
    # Add one to the current song number
    next_one = next_one[0]+1
    # Grab song title from playlist
    song = song_box.get(next_one)
    # Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear active bar in playlist
    song_box.selection_clear(0, END)
    # Activate new song bar
    song_box.activate(next_one)
    # Set active bar to next song
    song_box.selection_set(next_one, last=None)

# Play the previous song in the playlist
def prev_song():
    # Reset slider and duration bar
    dur_status.config(text='')
    my_slider.config(value=0)
    # Get the current song listed number
    prev_one = song_box.curselection()
    # Add one to the current song number
    prev_one = prev_one[0]-1
    # Grab song title from playlist
    song = song_box.get(prev_one)
    # Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear active bar in playlist
    song_box.selection_clear(0, END)
    # Activate new song bar
    song_box.activate(prev_one)
    # Set active bar to next song
    song_box.selection_set(prev_one, last=None)

# Remove Selected Song
def remove_song():
    stop()
    song_box.delete(ANCHOR)
    # Stop music if it's playing
    pygame.mixer.music.stop()

# Remove All Songs
def remove_all_songs():
    stop()
    song_box.delete(0, END)
    # Stop music if it's playing
    pygame.mixer.music.stop()

# Help Menu Functions
def openlink():
    fblink = 'https://www.facebook.com/arbeagles'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(fblink)

def ytlink():
    ytubelink = 'https://www.youtube.com/channel/UCmcGB8PNVxig1WGye-H3ZIA'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(ytubelink)

def devlink():
    cdlink = 'https://www.facebook.com/CrazyMido8'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(cdlink)

def aboutapp():
    showinfo("About ArabEagles Mp3 Player", "This App is designed by CrazyMido for ArabEagles!\nPlease follow us on Facebook and subscribe to our YouTube channel.")

# Get Song length and duration
def play_time():
    # check if song stopped to not double timing
    if stopped:
        return
    # Get current song elapsed time
    current_time = pygame.mixer.music.get_pos() / 1000
    # Convert to time format
    converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))
    # Grab song title from playlist
    song = song_box.get(ACTIVE)
    # Load song with Mutagen
    song_mut = MP3(song)
    # Get song length
    global song_length
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%H:%M:%S', time.gmtime(song_length))
    # Increase current time by 1 second
    current_time +=1
    if int(my_slider.get()) == int(song_length):
        dur_status.config(text=f'Time Elapsed: {converted_song_length} of {converted_song_length}  ')
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        # Update slider to position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # slider has been moved
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        converted_current_time = time.strftime('%H:%M:%S', time.gmtime(int(my_slider.get())))
        dur_status.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}  ')
        # move slider along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)
    # Updating Duration
    dur_status.after(1000, play_time)

# Create Slider Func.
def slide(x):
    song = song_box.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

# Create Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    # Get current volume
    current_volume = pygame.mixer.music.get_volume()
    # change time to be easier to work with volume meter
    current_volume = current_volume * 100
    # Change volume meter image
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 5:
        volume_meter.config(image=vol5)
    elif int(current_volume) > 5 and int(current_volume) <= 10:
        volume_meter.config(image=vol10)
    elif int(current_volume) > 10 and int(current_volume) <= 15:
        volume_meter.config(image=vol15)
    elif int(current_volume) > 15 and int(current_volume) <= 20:
        volume_meter.config(image=vol20)
    elif int(current_volume) > 20 and int(current_volume) <= 25:
        volume_meter.config(image=vol25)
    elif int(current_volume) > 25 and int(current_volume) <= 30:
        volume_meter.config(image=vol30)
    elif int(current_volume) > 30 and int(current_volume) <= 35:
        volume_meter.config(image=vol35)
    elif int(current_volume) > 35 and int(current_volume) <= 40:
        volume_meter.config(image=vol40)
    elif int(current_volume) > 40 and int(current_volume) <= 45:
        volume_meter.config(image=vol45)
    elif int(current_volume) > 45 and int(current_volume) <= 50:
        volume_meter.config(image=vol50)
    elif int(current_volume) > 50 and int(current_volume) <= 55:
        volume_meter.config(image=vol55)
    elif int(current_volume) > 55 and int(current_volume) <= 60:
        volume_meter.config(image=vol60)
    elif int(current_volume) > 60 and int(current_volume) <= 65:
        volume_meter.config(image=vol65)
    elif int(current_volume) > 65 and int(current_volume) <= 70:
        volume_meter.config(image=vol70)
    elif int(current_volume) > 70 and int(current_volume) <= 75:
        volume_meter.config(image=vol75)
    elif int(current_volume) > 75 and int(current_volume) <= 80:
        volume_meter.config(image=vol80)
    elif int(current_volume) > 80 and int(current_volume) <= 85:
        volume_meter.config(image=vol85)
    elif int(current_volume) > 85 and int(current_volume) <= 90:
        volume_meter.config(image=vol90)
    elif int(current_volume) > 90 and int(current_volume) <= 95:
        volume_meter.config(image=vol95)
    elif int(current_volume) > 95 and int(current_volume) <= 100:
        volume_meter.config(image=vol100)

# Create App Name Label
Label(root, fg="red", font=("Times",18,"bold")).pack(pady=13, anchor=W)

# Create Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Create Playlist Box
song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.grid(row=0,column=0,pady=10)

# Player Controlers Images
back_button_img = PhotoImage(file='back.png')
forward_button_img = PhotoImage(file='forward.png')
play_button_img = PhotoImage(file='play.png')
pause_button_img = PhotoImage(file='pause.png')
stop_button_img = PhotoImage(file='stop.png')

# Volume control images
global vol0
global vol5
global vol10
global vol15
global vol20
global vol25
global vol30
global vol35
global vol40
global vol45
global vol50
global vol55
global vol60
global vol65
global vol70
global vol75
global vol80
global vol85
global vol90
global vol95
global vol100
vol0 = PhotoImage(file='vol0.png')
vol5 = PhotoImage(file='vol5.png')
vol10 = PhotoImage(file='vol10.png')
vol15 = PhotoImage(file='vol15.png')
vol20 = PhotoImage(file='vol20.png')
vol25 = PhotoImage(file='vol25.png')
vol30 = PhotoImage(file='vol30.png')
vol35 = PhotoImage(file='vol35.png')
vol40 = PhotoImage(file='vol40.png')
vol45 = PhotoImage(file='vol45.png')
vol50 = PhotoImage(file='vol50.png')
vol55 = PhotoImage(file='vol55.png')
vol60 = PhotoImage(file='vol60.png')
vol65 = PhotoImage(file='vol65.png')
vol70 = PhotoImage(file='vol70.png')
vol75 = PhotoImage(file='vol75.png')
vol80 = PhotoImage(file='vol80.png')
vol85 = PhotoImage(file='vol85.png')
vol90 = PhotoImage(file='vol90.png')
vol95 = PhotoImage(file='vol95.png')
vol100 = PhotoImage(file='vol100.png')

# Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1,column=0,pady=5)

# Create Volume meter frame
volume_meter = Label(master_frame, image=vol100)
volume_meter.grid(row=1, column=1,padx=10)

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0,column=1,padx=20)

# Create Player Control Buttons
back_button = Button(controls_frame,image=back_button_img, borderwidth=0, command=prev_song)
forward_button = Button(controls_frame,image=forward_button_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame,image=play_button_img, borderwidth=0, command=play)
pause_button = Button(controls_frame,image=pause_button_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame,image=stop_button_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=5)
forward_button.grid(row=0, column=4, padx=5)
play_button.grid(row=0, column=1, padx=5)
pause_button.grid(row=0, column=2, padx=5)
stop_button.grid(row=0, column=3, padx=5)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)
add_song_menu.add_command(label="Add many Songs to Playlist", command=add__many_song)
add_song_menu.add_separator()
add_song_menu.add_command(label="Exit", command=root.quit)

# Delete Song Menu
remove_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Remove Selected Song", command=remove_song)
remove_song_menu.add_command(label="Remove All Songs", command=remove_all_songs)

# Add Help Menu
help_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="About", menu=help_menu)
help_menu.add_command(label="Our FaceBook Page", command=openlink)
help_menu.add_command(label="Our YouTube Channel", command=ytlink)
help_menu.add_command(label="Contact Developer", command=devlink)
help_menu.add_separator()
help_menu.add_command(label="About App", command=aboutapp)

# Create music position slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2,column=0,pady=10)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

# Create Duration status bar
dur_status = Label(root, text='', bd=1, relief=GROOVE, anchor=W)
dur_status.pack(fill=X, side=BOTTOM, padx=2, ipady=2)

# App Version Status Bar
appver_status = Label(root, text="Created by:CrazyMido - ver:1.0.0", fg="black", anchor=E)
appver_status.pack(fill=X, side=BOTTOM, padx=5)



root.mainloop()
