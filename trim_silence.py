import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

# Args
parser = argparse.ArgumentParser(description='Detect and remove silence from a video file.')
parser.add_argument('input', help='path to input video file')
parser.add_argument('output', help='path to output video file')
parser.add_argument('--threshold', type=int, default=-40,
                    help='threshold for silence detection in dB (default: -40)')

# Parse arguments
args = parser.parse_args()

# Open the video file and extract the audio track
input_video_path = args.input
output_video_path = args.output
video_clip = VideoFileClip(input_video_path)
audio_clip = video_clip.audio

# Calculate the average volume of the audio track
avg_volume = audio_clip.audio_norm_db

# Set the silence detection threshold
silence_threshold = args.threshold

# Initialize variables for keeping track of silence periods
silence_start = None
silence_end = None

# Iterate over the audio frames and detect silence periods
for t, frame in enumerate(audio_clip.iter_frames()):
    volume = audio_clip.get_frame(t, 'dB')
    if volume < silence_threshold:
        if silence_start is None:
            silence_start = t
    else:
        if silence_start is not None:
            silence_end = t
            # Remove the silence period from the audio and video clips
            start_time = silence_start / audio_clip.fps
            end_time = silence_end / audio_clip.fps
            audio_clip = audio_clip.subclip(0, start_time).\
                         append(audio_clip.subclip(end_time))
            video_clip = video_clip.subclip(0, start_time).\
                         append(video_clip.subclip(end_time))
            silence_start = None
            silence_end = None

# Write the new audio file without silence periods
cut_audio_path = 'cut_audio.wav'
audio_clip.write_audiofile(cut_audio_path)

# Use the new audio file to generate a new video clip without silence
new_video_clip = video_clip.set_audio(AudioFileClip(cut_audio_path))
new_video_clip.write_videofile(output_video_path)

# Clean up temporary files
video_clip.close()
new_video_clip.close()
audio_clip.close()
os.remove(cut_audio_path)
