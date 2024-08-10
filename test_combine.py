from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

video_file = 'C:\\Users\\GregR\\OneDrive\\Desktop\\panic\\recorded_video.mp4'  # Path to your video file
audio_file = 'C:\\Users\\GregR\\OneDrive\\Desktop\\panic\\recorded_audio.wav'  # Path to your audio file
output_file = 'combined_output.mp4'


def combine_video_audio(video_path, audio_path, output_filename):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_filename)


combine_video_audio(video_file, audio_file, output_file)

