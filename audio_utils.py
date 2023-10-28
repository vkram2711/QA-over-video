from moviepy.video.io.VideoFileClip import VideoFileClip


def download_audio(audio_url):
    # Load the video from the URL
    video_clip = VideoFileClip(audio_url)

    # Extract the audio
    audio_clip = video_clip.audio

    # Specify the output audio file name (e.g., 'output_audio.mp3')
    output_audio_path = 'output_audio.mp3'

    # Write the audio to a file
    audio_clip.write_audiofile(output_audio_path)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()