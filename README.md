# TrimSilence
Cut out silence from a video file, generating a new video without the silent parts.

The script takes a video file path, an output file path, and a file containing the timestamps of the silent parts of the video as input. It then uses the MoviePy library to split the video into clips at the points of silence, and concatenates the remaining clips to create a new video file without the silent parts. The ease parameter determines the duration of a fade-in effect applied to the beginning of each clip. The minimum_duration parameter sets the minimum duration of each clip to prevent short clips from being generated. The output video is encoded using the H.265 codec with the ultrafast preset, and a frame rate of 30 fps.
