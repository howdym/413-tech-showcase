from moviepy.editor import VideoFileClip

source_video  = VideoFileClip("timelapse_f54.mp4")
sped_up_video = source_video.speedx(factor=1.5)
sped_up_video.write_videofile("timelapse_f81.mp4")
