from test_aud import start_audio
from test_vid import start_video
import time
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import threading


video_file = 'C:\\Users\\GregR\\OneDrive\\Desktop\\panic\\recorded_video.mp4'  # Path to your video file
audio_file = 'C:\\Users\\GregR\\OneDrive\\Desktop\\panic\\recorded_audio.wav'  # Path to your audio file
output_file = 'combined_output.mp4'



# Create two threads
thread_audio = threading.Thread(target=start_audio)
thread_video = threading.Thread(target=start_video)

# Start both threads
thread_audio.start()
thread_video.start()

# Wait for both threads to finish
thread_audio.join()
thread_video.join()

print("delay the script 10 seconds...")

# Sleep for 10 seconds
time.sleep(10)


def combine_video_audio(video_path, audio_path, output_filename):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_filename)
    
combine_video_audio(video_file, audio_file, output_file)