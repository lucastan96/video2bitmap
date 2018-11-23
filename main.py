import moviepy.editor as mpy
import moviepy.video.fx.all as vfx
import subprocess as sp

# Crop and resize video
clip = mpy.VideoFileClip("smoke.mp4")
(w, h) = clip.size
cropped_clip = vfx.crop(clip, width=(h/128)*64, height=h, x1=w/4*3-100, y1=0).resize((64, 128))
cropped_clip.write_videofile('smoke-cropped.mp4')

# Convert video to frames
# Make sure to install ffmpeg on machine
cmd='ffmpeg -i /path/to/smoke-cropped.mp4 /path/to/frames_temp/%d.bmp'
sp.call(cmd,shell=True)

# Convert image to black and white bitmap
for i in range(202):
    col = Image.open("frames_temp/" + str(i + 1) + ".bmp")
    gray = col.convert('L')
    bw = gray.point(lambda x: 0 if x<128 else 255, '1')
    bw.save("frames/" + str(i) + ".bmp")