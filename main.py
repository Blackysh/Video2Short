import tkinter
import customtkinter
import os                               # importing the os module  
import shutil
from pytube import YouTube 
from tkinter import filedialog as fd
from moviepy import *
from moviepy.editor import *
import editor
from editor import start
from tkinter import messagebox

os.system("rm -r TEMP/")
os.system("del /F /Q TEMP")
os.system('mkdir TEMP')

#Set Appearance
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")
app.title("EasyShorts")
app.resizable(False, False)



starting_value = 0
video_duration = 0
ending_value = 59
placement = 'Center'
def optionmenu_callback(choice):
    global placement
    placement = str(choice)


def vidSelectedButtons(video_duration):
    global textbox1
    global textbox
    label = customtkinter.CTkLabel(master=app, text="Clip start(secs)")
    label.place(relx=0.43, rely=0.31, anchor=tkinter.CENTER)
    label = customtkinter.CTkLabel(master=app, text="Clip end(secs)")
    label.place(relx=0.43, rely=0.41, anchor=tkinter.CENTER)
    textbox = customtkinter.CTkTextbox(master=app, width=200, height=10, corner_radius=0, border_color="white", border_width=2)
    textbox.grid(row=0, column=0, sticky="nsew")
    textbox.insert("0.0", str(video_duration))
    textbox.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
    textbox1 = customtkinter.CTkTextbox(master=app, width=200, height=10, corner_radius=0, border_color="white", border_width=2)
    textbox1.grid(row=0, column=0, sticky="nsew")
    textbox1.insert("0.0", "0.0")
    textbox1.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    placement = customtkinter.StringVar(value="Center")  # set initial value
    combobox = customtkinter.CTkOptionMenu(master=app,
                                     values=["Left", "Center", "Right", "Boxed"],
                                     variable=placement, width=200, command=optionmenu_callback)
    combobox.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=app, width=250, height=52, text="Render", command=exporting)
    button.place(relx = 0.5, rely = 0.8, anchor=tkinter.CENTER)




def openFile():  
   # selecting the file using the askopenfilename() method of filedialog
    global video_duration
    global video
    os.system("del /F /Q TEMP")
    videoe = fd.askopenfilename(  
      title = "Select a video",  
      filetypes = [("videos", "*.mp4 *.mov *.avi")]
      )  
    print(videoe)
    shutil.copyfile(videoe, "TEMP/video.mp4")
    
    video = "TEMP/video.mp4"
    video_duration = VideoFileClip(video).duration
    vidSelectedButtons(video_duration)

    

def videoYT():
    global video_duration
    global video
    os.system("del /F /Q TEMP")
    videoYT = customtkinter.CTkInputDialog(text="Youtube Video Link", title="Paste Link")
    videoYT = videoYT.get_input()
    YouTube(videoYT).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("TEMP/" , "video.mp4")
    print("done Downloading")
    video = "TEMP/video.mp4"
    video_duration = VideoFileClip(video).duration
    vidSelectedButtons(video_duration)

button = customtkinter.CTkButton(master=app, width=250, height=52, text="Select Video (Locally)", command=openFile)
button.place(relx = 0.5, rely = 0.1, anchor=tkinter.CENTER)
button = customtkinter.CTkButton(master=app, width=250, height=52, text="Youtube Link", command=videoYT)
button.place(relx = 0.5, rely = 0.2, anchor=tkinter.CENTER)

def exporting():
    starting_value = textbox1.get("0.0", "end")
    ending_value = textbox.get("0.0", "end")
    print( str(video_duration) + "\n" + str(placement) + "\n" + str(starting_value)  + "\n" +  str(ending_value) + "\n" + str(video))


    if float(starting_value) > float(ending_value) or float(ending_value) > float(video_duration) or float(starting_value) == float(ending_value) or float(starting_value) == float(video_duration):
        messagebox.showerror('Wrong Values', 'Error: Recheck values, the values are wrong.')


    else:
        start(placement=str(placement), starting_valu=float(starting_value), ending_valu=float(ending_value))

app.mainloop()
