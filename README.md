# TrimSilence 🤫🎬
### Cut out silence from a video file, generating a new video without the silent parts.

The script takes a video file path, an output file path, and a threshold value as input. It then uses the MoviePy library to split the video into clips at the points of silence, and concatenates the remaining clips to create a new video file without the silent parts. The --threshold option sets the volume threshold below which a frame is considered silent. You can adjust this value to fine-tune the silence detection.

#### Dependencies
- Python 3.6 or higher
- [moviepy](https://pypi.org/project/moviepy/) library

#### Usage
To remove silence from a video file, run the command:
`python trim_silence.py input_file output_file [--threshold THRESHOLD]`

##### Parameters:
- `input_file`: path to the input video
- `output_file`: path to the output video
- `--threshold`: threshold for silence detection in dB (default: -40)

#### Example

Here's an example command to cut out silent parts of a video:

`python trim_silence.py input.mp4 output.mp4 --threshold -45`

This will remove any periods of silence in the video file where the volume drops below -45 dB.
