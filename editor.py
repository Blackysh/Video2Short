from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import crop
from moviepy.video.fx.all import margin
import os

video = "TEMP/video.mp4"



def start(placement, starting_valu, ending_valu):
    os.system('del /F /Q Final.mp4')
    os.system('rm -r Final.mp4')

    global starting_value
    global ending_value
    global video_width
    global video

    global w, h

    starting_value = starting_valu
    ending_value = ending_valu

    video = VideoFileClip("TEMP/video.mp4").subclip(starting_value, ending_value)
    (w, h) = video.size
    video_width = h * 9/16
    print(w)

    if placement == "Left":
        Left(video, video_width)
    elif placement == "Right":
        Right(video, video_width)
    elif placement == "Center":
        Center(video, video_width)
    elif placement == "Boxed":
        Boxed(video, video_width)
    
    else: # Custom layout
        print(placement)



    return



def Left(video, video_width):
    x1, x2 = 0, (w-video_width)//2
    y1, y2 = 0, h
    video = crop(video, x1=x1, y1=y1, x2=x2, y2=y2)
    video.write_videofile("Final.mp4")

    return

def Center(video, video_width):
    video_widthe = video_width
    print(video_widthe)
    video = crop(video, width=video_width, height=h, x_center=w/2, y_center=h/2)
    video.write_videofile("Final.mp4")
    return

def Right(video, video_width):
    x1, x2 = (w+video_width)//2, 0
    y1, y2 = 0, h
    video = crop(video, x1=x1, y1=y1, x2=x2, y2=y2)
    video.write_videofile("Final.mp4")
    return


def Boxed(video, video_width):
    x = w / 9
    total_margin = x * 16
    total_margin = total_margin - h
    half_margin = int(total_margin / 2)

    video = video.margin(top=half_margin, bottom=half_margin) 
    video.write_videofile("Final.mp4") 
    return 



